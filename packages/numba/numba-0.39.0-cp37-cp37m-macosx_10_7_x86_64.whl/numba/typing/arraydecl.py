from __future__ import print_function, division, absolute_import

import numpy as np

from collections import namedtuple

from numba import types, utils
from numba.typing.templates import (AttributeTemplate, AbstractTemplate,
                                    infer, infer_getattr, signature,
                                    bound_function)
# import time side effect: array operations requires typing support of sequence
# defined in collections: e.g. array.shape[i]
from numba.typing import collections
from numba.errors import TypingError

Indexing = namedtuple("Indexing", ("index", "result", "advanced"))


def get_array_index_type(ary, idx):
    """
    Returns None or a tuple-3 for the types of the input array, index, and
    resulting type of ``array[index]``.

    Note: This is shared logic for ndarray getitem and setitem.
    """
    if not isinstance(ary, types.Buffer):
        return

    ndim = ary.ndim

    left_indices = []
    right_indices = []
    ellipsis_met = False
    advanced = False
    has_integer = False

    if not isinstance(idx, types.BaseTuple):
        idx = [idx]

    # Walk indices
    for ty in idx:
        if ty is types.ellipsis:
            if ellipsis_met:
                raise TypeError("only one ellipsis allowed in array index "
                                "(got %s)" % (idx,))
            ellipsis_met = True
        elif isinstance(ty, types.SliceType):
            pass
        elif isinstance(ty, types.Integer):
            # Normalize integer index
            ty = types.intp if ty.signed else types.uintp
            # Integer indexing removes the given dimension
            ndim -= 1
            has_integer = True
        elif (isinstance(ty, types.Array) and ty.ndim == 0
              and isinstance(ty.dtype, types.Integer)):
            # 0-d array used as integer index
            ndim -= 1
            has_integer = True
        elif (isinstance(ty, types.Array)
              and ty.ndim == 1
              and isinstance(ty.dtype, (types.Integer, types.Boolean))):
            if advanced or has_integer:
                # We don't support the complicated combination of
                # advanced indices (and integers are considered part
                # of them by Numpy).
                raise NotImplementedError("only one advanced index supported")
            advanced = True
        else:
            raise TypeError("unsupported array index type %s in %s"
                            % (ty, idx))
        (right_indices if ellipsis_met else left_indices).append(ty)

    # Only Numpy arrays support advanced indexing
    if advanced and not isinstance(ary, types.Array):
        return

    # Check indices and result dimensionality
    all_indices = left_indices + right_indices
    if ellipsis_met:
        assert right_indices[0] is types.ellipsis
        del right_indices[0]

    n_indices = len(all_indices) - ellipsis_met
    if n_indices > ary.ndim:
        raise TypeError("cannot index %s with %d indices: %s"
                        % (ary, n_indices, idx))
    if n_indices == ary.ndim and ndim == 0 and not ellipsis_met:
        # Full integer indexing => scalar result
        # (note if ellipsis is present, a 0-d view is returned instead)
        res = ary.dtype

    elif advanced:
        # Result is a copy
        res = ary.copy(ndim=ndim, layout='C', readonly=False)

    else:
        # Result is a view
        if ary.slice_is_copy:
            # Avoid view semantics when the original type creates a copy
            # when slicing.
            return

        # Infer layout
        layout = ary.layout

        def keeps_contiguity(ty, is_innermost):
            # A slice can only keep an array contiguous if it is the
            # innermost index and it is not strided
            return (ty is types.ellipsis or isinstance(ty, types.Integer)
                    or (is_innermost and isinstance(ty, types.SliceType)
                        and not ty.has_step))

        def check_contiguity(outer_indices):
            """
            Whether indexing with the given indices (from outer to inner in
            physical layout order) can keep an array contiguous.
            """
            for ty in outer_indices[:-1]:
                if not keeps_contiguity(ty, False):
                    return False
            if outer_indices and not keeps_contiguity(outer_indices[-1], True):
                return False
            return True

        if layout == 'C':
            # Integer indexing on the left keeps the array C-contiguous
            if n_indices == ary.ndim:
                # If all indices are there, ellipsis's place is indifferent
                left_indices = left_indices + right_indices
                right_indices = []
            if right_indices:
                layout = 'A'
            elif not check_contiguity(left_indices):
                layout = 'A'
        elif layout == 'F':
            # Integer indexing on the right keeps the array F-contiguous
            if n_indices == ary.ndim:
                # If all indices are there, ellipsis's place is indifferent
                right_indices = left_indices + right_indices
                left_indices = []
            if left_indices:
                layout = 'A'
            elif not check_contiguity(right_indices[::-1]):
                layout = 'A'

        res = ary.copy(ndim=ndim, layout=layout)

    # Re-wrap indices
    if isinstance(idx, types.BaseTuple):
        idx = types.BaseTuple.from_types(all_indices)
    else:
        idx, = all_indices

    return Indexing(idx, res, advanced)


@infer
class GetItemBuffer(AbstractTemplate):
    key = "getitem"

    def generic(self, args, kws):
        assert not kws
        [ary, idx] = args
        out = get_array_index_type(ary, idx)
        if out is not None:
            return signature(out.result, ary, out.index)

@infer
class SetItemBuffer(AbstractTemplate):
    key = "setitem"

    def generic(self, args, kws):
        assert not kws
        ary, idx, val = args
        if not isinstance(ary, types.Buffer):
            return
        if not ary.mutable:
            raise TypeError("Cannot modify value of type %s" %(ary,))
        out = get_array_index_type(ary, idx)
        if out is None:
            return

        idx = out.index
        res = out.result
        if isinstance(res, types.Array):
            # Indexing produces an array
            if isinstance(val, types.Array):
                if not self.context.can_convert(val.dtype, res.dtype):
                    # DType conversion not possible
                    return
                else:
                    res = val
            elif isinstance(val, types.Sequence):
                if (res.ndim == 1 and
                    self.context.can_convert(val.dtype, res.dtype)):
                    # Allow assignement of sequence to 1d array
                    res = val
                else:
                    # NOTE: sequence-to-array broadcasting is unsupported
                    return
            else:
                # Allow scalar broadcasting
                if self.context.can_convert(val, res.dtype):
                    res = res.dtype
                else:
                    # Incompatible scalar type
                    return
        elif not isinstance(val, types.Array):
            # Single item assignment
            if not self.context.can_convert(val, res):
                # if the array dtype is not yet defined
                if not res.is_precise():
                    # set the array type to use the dtype of value (RHS)
                    newary = ary.copy(dtype=val)
                    return signature(types.none, newary, idx, res)
                else:
                    return
            res = val
        else:
            return
        return signature(types.none, ary, idx, res)


def normalize_shape(shape):
    if isinstance(shape, types.UniTuple):
        if isinstance(shape.dtype, types.Integer):
            dimtype = types.intp if shape.dtype.signed else types.uintp
            return types.UniTuple(dimtype, len(shape))

    elif isinstance(shape, types.Tuple) and shape.count == 0:
        # Force (0 x intp) for consistency with other shapes
        return types.UniTuple(types.intp, 0)


@infer_getattr
class ArrayAttribute(AttributeTemplate):
    key = types.Array

    def resolve_dtype(self, ary):
        return types.DType(ary.dtype)

    def resolve_itemsize(self, ary):
        return types.intp

    def resolve_shape(self, ary):
        return types.UniTuple(types.intp, ary.ndim)

    def resolve_strides(self, ary):
        return types.UniTuple(types.intp, ary.ndim)

    def resolve_ndim(self, ary):
        return types.intp

    def resolve_size(self, ary):
        return types.intp

    def resolve_flat(self, ary):
        return types.NumpyFlatType(ary)

    def resolve_ctypes(self, ary):
        return types.ArrayCTypes(ary)

    def resolve_flags(self, ary):
        return types.ArrayFlags(ary)

    def resolve_T(self, ary):
        if ary.ndim <= 1:
            retty = ary
        else:
            layout = {"C": "F", "F": "C"}.get(ary.layout, "A")
            retty = ary.copy(layout=layout)
        return retty

    def resolve_real(self, ary):
        return self._resolve_real_imag(ary, attr='real')

    def resolve_imag(self, ary):
        return self._resolve_real_imag(ary, attr='imag')

    def _resolve_real_imag(self, ary, attr):
        if ary.dtype in types.complex_domain:
            return ary.copy(dtype=ary.dtype.underlying_float, layout='A')
        elif ary.dtype in types.number_domain:
            res = ary.copy(dtype=ary.dtype)
            if attr == 'imag':
                res = res.copy(readonly=True)
            return res
        else:
            msg = "cannot access .{} of array of {}"
            raise TypingError(msg.format(attr, ary.dtype))

    @bound_function("array.transpose")
    def resolve_transpose(self, ary, args, kws):
        def sentry_shape_scalar(ty):
            if ty in types.number_domain:
                # Guard against non integer type
                if not isinstance(ty, types.Integer):
                    raise TypeError("transpose() arg cannot be {0}".format(ty))
                return True
            else:
                return False

        assert not kws
        if len(args) == 0:
            return signature(self.resolve_T(ary))

        if len(args) == 1:
            shape, = args

            if sentry_shape_scalar(shape):
                assert ary.ndim == 1
                return signature(ary, *args)

            shape = normalize_shape(shape)
            if shape is None:
                return

            assert ary.ndim == shape.count
            return signature(self.resolve_T(ary), shape)

        else:
            if any(not sentry_shape_scalar(a) for a in args):
                raise TypeError("transpose({0}) is not supported".format(
                    ', '.join(args)))
            assert ary.ndim == len(args)
            return signature(self.resolve_T(ary), *args)

    @bound_function("array.copy")
    def resolve_copy(self, ary, args, kws):
        assert not args
        assert not kws
        retty = ary.copy(layout="C", readonly=False)
        return signature(retty)

    @bound_function("array.item")
    def resolve_item(self, ary, args, kws):
        assert not kws
        # We don't support explicit arguments as that's exactly equivalent
        # to regular indexing.  The no-argument form is interesting to
        # allow some degree of genericity when writing functions.
        if not args:
            return signature(ary.dtype)

    @bound_function("array.itemset")
    def resolve_itemset(self, ary, args, kws):
        assert not kws
        # We don't support explicit arguments as that's exactly equivalent
        # to regular indexing.  The no-argument form is interesting to
        # allow some degree of genericity when writing functions.
        if len(args) == 1:
            return signature(types.none, ary.dtype)

    @bound_function("array.nonzero")
    def resolve_nonzero(self, ary, args, kws):
        assert not args
        assert not kws
        # 0-dim arrays return one result array
        ndim = max(ary.ndim, 1)
        retty = types.UniTuple(types.Array(types.intp, 1, 'C'), ndim)
        return signature(retty)

    @bound_function("array.reshape")
    def resolve_reshape(self, ary, args, kws):
        def sentry_shape_scalar(ty):
            if ty in types.number_domain:
                # Guard against non integer type
                if not isinstance(ty, types.Integer):
                    raise TypeError("reshape() arg cannot be {0}".format(ty))
                return True
            else:
                return False

        assert not kws
        if ary.layout not in 'CF':
            # only work for contiguous array
            raise TypeError("reshape() supports contiguous array only")

        if len(args) == 1:
            # single arg
            shape, = args

            if sentry_shape_scalar(shape):
                ndim = 1
            else:
                shape = normalize_shape(shape)
                if shape is None:
                    return
                ndim = shape.count
            retty = ary.copy(ndim=ndim)
            return signature(retty, shape)

        elif len(args) == 0:
            # no arg
            raise TypeError("reshape() take at least one arg")

        else:
            # vararg case
            if any(not sentry_shape_scalar(a) for a in args):
                raise TypeError("reshape({0}) is not supported".format(
                    ', '.join(args)))

            retty = ary.copy(ndim=len(args))
            return signature(retty, *args)

    @bound_function("array.sort")
    def resolve_sort(self, ary, args, kws):
        assert not args
        assert not kws
        if ary.ndim == 1:
            return signature(types.none)

    @bound_function("array.argsort")
    def resolve_argsort(self, ary, args, kws):
        assert not args
        kwargs = dict(kws)
        kind = kwargs.pop('kind', types.Const('quicksort'))
        if kwargs:
            msg = "Unsupported keywords: {!r}"
            raise TypingError(msg.format([k for k in kwargs.keys()]))
        if ary.ndim == 1:
            def argsort_stub(kind='quicksort'):
                pass
            pysig = utils.pysignature(argsort_stub)
            sig = signature(types.Array(types.intp, 1, 'C'), kind).replace(pysig=pysig)
            return sig

    @bound_function("array.view")
    def resolve_view(self, ary, args, kws):
        from .npydecl import _parse_dtype
        assert not kws
        dtype, = args
        dtype = _parse_dtype(dtype)
        if dtype is None:
            return
        retty = ary.copy(dtype=dtype)
        return signature(retty, *args)

    @bound_function("array.astype")
    def resolve_astype(self, ary, args, kws):
        from .npydecl import _parse_dtype
        assert not kws
        dtype, = args
        dtype = _parse_dtype(dtype)
        if dtype is None:
            return
        if not self.context.can_convert(ary.dtype, dtype):
            raise TypeError("astype(%s) not supported on %s: "
                            "cannot convert from %s to %s"
                            % (dtype, ary, ary.dtype, dtype))
        layout = ary.layout if ary.layout in 'CF' else 'C'
        retty = ary.copy(dtype=dtype, layout=layout)
        return signature(retty, *args)

    @bound_function("array.ravel")
    def resolve_ravel(self, ary, args, kws):
        # Only support no argument version (default order='C')
        assert not kws
        assert not args
        return signature(ary.copy(ndim=1, layout='C'))

    @bound_function("array.flatten")
    def resolve_flatten(self, ary, args, kws):
        # Only support no argument version (default order='C')
        assert not kws
        assert not args
        return signature(ary.copy(ndim=1, layout='C'))

    @bound_function("array.take")
    def resolve_take(self, ary, args, kws):
        assert not kws
        argty, = args
        if isinstance(argty, types.Integer):
            sig = signature(ary.dtype, *args)
        elif isinstance(argty, types.Array):
            sig = signature(argty.copy(layout='C', dtype=ary.dtype), *args)
        elif isinstance(argty, types.List): # 1d lists only
            sig = signature(types.Array(ary.dtype, 1, 'C'), *args)
        elif isinstance(argty, types.BaseTuple):
            sig = signature(types.Array(ary.dtype, np.ndim(argty), 'C'), *args)
        else:
            raise TypeError("take(%s) not supported for %s" % argty)
        return sig

    def generic_resolve(self, ary, attr):
        # Resolution of other attributes, for record arrays
        if isinstance(ary.dtype, types.Record):
            if attr in ary.dtype.fields:
                return ary.copy(dtype=ary.dtype.typeof(attr), layout='A')


@infer_getattr
class DTypeAttr(AttributeTemplate):
    key = types.DType

    def resolve_type(self, ary):
        # Wrap the numeric type in NumberClass
        return types.NumberClass(ary.dtype)

    def resolve_kind(self, ary):
        if isinstance(ary.key, types.scalars.Float):
            val = 'f'
        elif isinstance(ary.key, types.scalars.Integer):
            val = 'i'
        else:
            return None  # other types not supported yet
        return types.Const(val)

@infer
class StaticGetItemArray(AbstractTemplate):
    key = "static_getitem"

    def generic(self, args, kws):
        # Resolution of members for record and structured arrays
        ary, idx = args
        if (isinstance(ary, types.Array) and isinstance(idx, str) and
            isinstance(ary.dtype, types.Record)):
            if idx in ary.dtype.fields:
                return ary.copy(dtype=ary.dtype.typeof(idx), layout='A')


@infer_getattr
class RecordAttribute(AttributeTemplate):
    key = types.Record

    def generic_resolve(self, record, attr):
        ret = record.typeof(attr)
        assert ret
        return ret

@infer
class StaticGetItemRecord(AbstractTemplate):
    key = "static_getitem"

    def generic(self, args, kws):
        # Resolution of members for records
        record, idx = args
        if isinstance(record, types.Record) and isinstance(idx, str):
            ret = record.typeof(idx)
            assert ret
            return ret

@infer
class StaticSetItemRecord(AbstractTemplate):
    key = "static_setitem"

    def generic(self, args, kws):
        # Resolution of members for record and structured arrays
        record, idx, value = args
        if isinstance(record, types.Record) and isinstance(idx, str):
            expectedty = record.typeof(idx)
            if self.context.can_convert(value, expectedty) is not None:
                return signature(types.void, record, types.Const(idx), value)


@infer_getattr
class ArrayCTypesAttribute(AttributeTemplate):
    key = types.ArrayCTypes

    def resolve_data(self, ctinfo):
        return types.uintp


@infer_getattr
class ArrayFlagsAttribute(AttributeTemplate):
    key = types.ArrayFlags

    def resolve_contiguous(self, ctflags):
        return types.boolean

    def resolve_c_contiguous(self, ctflags):
        return types.boolean

    def resolve_f_contiguous(self, ctflags):
        return types.boolean


@infer_getattr
class NestedArrayAttribute(ArrayAttribute):
    key = types.NestedArray


def _expand_integer(ty):
    """
    If *ty* is an integer, expand it to a machine int (like Numpy).
    """
    if isinstance(ty, types.Integer):
        if ty.signed:
            return max(types.intp, ty)
        else:
            return max(types.uintp, ty)
    elif isinstance(ty, types.Boolean):
        return types.intp
    else:
        return ty

def generic_homog(self, args, kws):
    assert not args
    assert not kws
    return signature(self.this.dtype, recvr=self.this)

def generic_expand(self, args, kws):
    assert not args
    assert not kws
    return signature(_expand_integer(self.this.dtype), recvr=self.this)

def sum_expand(self, args, kws):
    """
    sum can be called with or without an axis parameter.
    """
    pysig = None
    if kws:
        def sum_stub(axis):
            pass
        pysig = utils.pysignature(sum_stub)
        # rewrite args
        args = list(args) + [kws['axis']]
        kws = None
    args_len = len(args)
    assert args_len <= 1
    if args_len == 0:
        # No axis parameter so the return type of the summation is a scalar
        # of the type of the array.
        out = signature(_expand_integer(self.this.dtype), *args,
                        recvr=self.this)
    else:
        # There is an axis paramter so the return type of this summation is
        # an array of dimension one less than the input array.
        return_type = types.Array(dtype=_expand_integer(self.this.dtype),
                                  ndim=self.this.ndim-1, layout='C')
        out = signature(return_type, *args, recvr=self.this)
    return out.replace(pysig=pysig)

def generic_expand_cumulative(self, args, kws):
    assert not args
    assert not kws
    assert isinstance(self.this, types.Array)
    return_type = types.Array(dtype=_expand_integer(self.this.dtype),
                              ndim=1, layout='C')
    return signature(return_type, recvr=self.this)

def generic_hetero_real(self, args, kws):
    assert not args
    assert not kws
    if isinstance(self.this.dtype, (types.Integer, types.Boolean)):
        return signature(types.float64, recvr=self.this)
    return signature(self.this.dtype, recvr=self.this)

def generic_index(self, args, kws):
    assert not args
    assert not kws
    return signature(types.intp, recvr=self.this)

def install_array_method(name, generic, support_literals=False):
    my_attr = {"key": "array." + name, "generic": generic}
    temp_class = type("Array_" + name, (AbstractTemplate,), my_attr)
    if support_literals:
        temp_class.support_literals = support_literals
    def array_attribute_attachment(self, ary):
        return types.BoundFunction(temp_class, ary)

    setattr(ArrayAttribute, "resolve_" + name, array_attribute_attachment)

# Functions that return the same type as the array
for fname in ["min", "max"]:
    install_array_method(fname, generic_homog)

# Functions that return a machine-width type, to avoid overflows
install_array_method("prod", generic_expand)
install_array_method("sum", sum_expand, support_literals=True)

# Functions that return a machine-width type, to avoid overflows
for fname in ["cumsum", "cumprod"]:
    install_array_method(fname, generic_expand_cumulative)

# Functions that require integer arrays get promoted to float64 return
for fName in ["mean", "var", "std"]:
    install_array_method(fName, generic_hetero_real)

# Functions that return an index (intp)
install_array_method("argmin", generic_index)
install_array_method("argmax", generic_index)


@infer
class CmpOpEqArray(AbstractTemplate):
    key = '=='

    def generic(self, args, kws):
        assert not kws
        [va, vb] = args
        if isinstance(va, types.Array) and va == vb:
            return signature(va.copy(dtype=types.boolean), va, vb)
