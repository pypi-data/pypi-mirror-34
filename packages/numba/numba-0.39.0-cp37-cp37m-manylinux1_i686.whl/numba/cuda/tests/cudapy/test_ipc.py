from __future__ import absolute_import, print_function, division

import sys
import multiprocessing as mp
import traceback
import pickle

import numpy as np

from numba import cuda
from numba.cuda.cudadrv import drvapi, devicearray
from numba import unittest_support as unittest
from numba.cuda.testing import skip_on_cudasim, CUDATestCase


not_linux = not sys.platform.startswith('linux')
has_mp_get_context = hasattr(mp, 'get_context')


def core_ipc_handle_test(the_work, result_queue):
    try:
        arr = the_work()
    except:
        # FAILED. propagate the exception as a string
        succ = False
        out = traceback.format_exc()
    else:
        # OK. send the ndarray back
        succ = True
        out = arr
    result_queue.put((succ, out))


def base_ipc_handle_test(handle, size, result_queue):
    def the_work():
        dtype = np.dtype(np.intp)
        with cuda.open_ipc_array(handle, shape=size // dtype.itemsize,
                                 dtype=dtype) as darr:
            # copy the data to host
            return darr.copy_to_host()

    core_ipc_handle_test(the_work, result_queue)


def serialize_ipc_handle_test(handle, result_queue):
    def the_work():
        dtype = np.dtype(np.intp)
        darr = handle.open_array(cuda.current_context(),
                                 shape=handle.size // dtype.itemsize,
                                 dtype=dtype)
        # copy the data to host
        arr = darr.copy_to_host()
        handle.close()
        return arr

    core_ipc_handle_test(the_work, result_queue)


def ipc_array_test(ipcarr, result_queue):
    try:
        with ipcarr as darr:
            arr = darr.copy_to_host()
            try:
                # should fail to reopen
                with ipcarr:
                    pass
            except ValueError as e:
                if str(e) != 'IpcHandle is already opened':
                    raise AssertionError('invalid exception message')
            else:
                raise AssertionError('did not raise on reopen')

    except:
        # FAILED. propagate the exception as a string
        succ = False
        out = traceback.format_exc()
    else:
        # OK. send the ndarray back
        succ = True
        out = arr
    result_queue.put((succ, out))


@unittest.skipIf(not_linux, "IPC only supported on Linux")
@unittest.skipUnless(has_mp_get_context, "requires multiprocessing.get_context")
@skip_on_cudasim('Ipc not available in CUDASIM')
class TestIpcMemory(CUDATestCase):
    def test_ipc_handle(self):
        # prepare data for IPC
        arr = np.arange(10, dtype=np.intp)
        devarr = cuda.to_device(arr)

        # create IPC handle
        ctx = cuda.current_context()
        ipch = ctx.get_ipc_handle(devarr.gpu_data)

        # manually prepare for serialization as bytes
        handle_bytes = bytes(ipch.handle)
        size = ipch.size

        # spawn new process for testing
        ctx = mp.get_context('spawn')
        result_queue = ctx.Queue()
        args = (handle_bytes, size, result_queue)
        proc = ctx.Process(target=base_ipc_handle_test, args=args)
        proc.start()
        succ, out = result_queue.get()
        if not succ:
            self.fail(out)
        else:
            np.testing.assert_equal(arr, out)
        proc.join(3)

    def test_ipc_handle_serialization(self):
        # prepare data for IPC
        arr = np.arange(10, dtype=np.intp)
        devarr = cuda.to_device(arr)

        # create IPC handle
        ctx = cuda.current_context()
        ipch = ctx.get_ipc_handle(devarr.gpu_data)

        # pickle
        buf = pickle.dumps(ipch)
        ipch_recon = pickle.loads(buf)
        self.assertIs(ipch_recon.base, None)
        self.assertEqual(tuple(ipch_recon.handle), tuple(ipch.handle))
        self.assertEqual(ipch_recon.size, ipch.size)

        # spawn new process for testing
        ctx = mp.get_context('spawn')
        result_queue = ctx.Queue()
        args = (ipch, result_queue)
        proc = ctx.Process(target=serialize_ipc_handle_test, args=args)
        proc.start()
        succ, out = result_queue.get()
        if not succ:
            self.fail(out)
        else:
            np.testing.assert_equal(arr, out)
        proc.join(3)

    def test_ipc_array(self):
        # prepare data for IPC
        arr = np.arange(10, dtype=np.intp)
        devarr = cuda.to_device(arr)
        ipch = devarr.get_ipc_handle()

        # spawn new process for testing
        ctx = mp.get_context('spawn')
        result_queue = ctx.Queue()
        args = (ipch, result_queue)
        proc = ctx.Process(target=ipc_array_test, args=args)
        proc.start()
        succ, out = result_queue.get()
        if not succ:
            self.fail(out)
        else:
            np.testing.assert_equal(arr, out)
        proc.join(3)


@unittest.skipUnless(not_linux, "Only on OS other than Linux")
@skip_on_cudasim('Ipc not available in CUDASIM')
class TestIpcNotSupported(CUDATestCase):
    def test_unsupported(self):
        arr = np.arange(10, dtype=np.intp)
        devarr = cuda.to_device(arr)
        with self.assertRaises(OSError) as raises:
            devarr.get_ipc_handle()
        errmsg = str(raises.exception)
        self.assertIn('OS does not support CUDA IPC', errmsg)


def staged_ipc_handle_test(handle, device_num, result_queue):
    def the_work():
        with cuda.gpus[device_num]:
            this_ctx = cuda.devices.get_context()
            can_access = handle.can_access_peer(this_ctx)
            print('can_access_peer {} {}'.format(this_ctx, can_access))
            deviceptr = handle.open_staged(this_ctx)
            arrsize = handle.size // np.dtype(np.intp).itemsize
            hostarray = np.zeros(arrsize, dtype=np.intp)
            cuda.driver.device_to_host(
                hostarray, deviceptr,  size=handle.size,
                )
            handle.close()
        return hostarray

    core_ipc_handle_test(the_work, result_queue)


def staged_ipc_array_test(ipcarr, device_num, result_queue):
    try:
        with cuda.gpus[device_num]:
            this_ctx = cuda.devices.get_context()
            print(this_ctx.device)
            with ipcarr as darr:
                arr = darr.copy_to_host()
                try:
                    # should fail to reopen
                    with ipcarr:
                        pass
                except ValueError as e:
                    if str(e) != 'IpcHandle is already opened':
                        raise AssertionError('invalid exception message')
                else:
                    raise AssertionError('did not raise on reopen')
    except:
        # FAILED. propagate the exception as a string
        succ = False
        out = traceback.format_exc()
    else:
        # OK. send the ndarray back
        succ = True
        out = arr
    result_queue.put((succ, out))


@unittest.skipIf(not_linux, "IPC only supported on Linux")
@unittest.skipUnless(has_mp_get_context, "requires multiprocessing.get_context")
@skip_on_cudasim('Ipc not available in CUDASIM')
class TestIpcStaged(CUDATestCase):
    def test_staged(self):
        # prepare data for IPC
        arr = np.arange(10, dtype=np.intp)
        devarr = cuda.to_device(arr)

        # spawn new process for testing
        mpctx = mp.get_context('spawn')
        result_queue = mpctx.Queue()

        # create IPC handle
        ctx = cuda.current_context()
        ipch = ctx.get_ipc_handle(devarr.gpu_data)
        # pickle
        buf = pickle.dumps(ipch)
        ipch_recon = pickle.loads(buf)
        self.assertIs(ipch_recon.base, None)
        self.assertEqual(tuple(ipch_recon.handle), tuple(ipch.handle))
        self.assertEqual(ipch_recon.size, ipch.size)

        # Test on every CUDA devices
        for device_num in range(len(cuda.gpus)):
            args = (ipch, device_num, result_queue)
            proc = mpctx.Process(target=staged_ipc_handle_test, args=args)
            proc.start()
            succ, out = result_queue.get()
            proc.join(3)
            if not succ:
                self.fail(out)
            else:
                np.testing.assert_equal(arr, out)

    def test_ipc_array(self):
        for device_num in range(len(cuda.gpus)):
            # prepare data for IPC
            arr = np.random.random(10)
            devarr = cuda.to_device(arr)
            ipch = devarr.get_ipc_handle()

            # spawn new process for testing
            ctx = mp.get_context('spawn')
            result_queue = ctx.Queue()
            args = (ipch, device_num, result_queue)
            proc = ctx.Process(target=staged_ipc_array_test, args=args)
            proc.start()
            succ, out = result_queue.get()
            proc.join(3)
            if not succ:
                self.fail(out)
            else:
                np.testing.assert_equal(arr, out)


if __name__ == '__main__':
    unittest.main()
