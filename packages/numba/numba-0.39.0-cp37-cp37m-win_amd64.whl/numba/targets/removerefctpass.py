"""
Implement a rewrite pass on LLVM module to remove unnecessary refcount
operation.
"""
from __future__ import absolute_import, print_function

from llvmlite.ir.transforms import CallVisitor

from numba import types


class _MarkNrtCallVisitor(CallVisitor):
    """
    A pass to mark all NRT_incref and NRT_decref.
    """
    def __init__(self):
        self.marked = set()

    def visit_Call(self, instr):
        if instr.callee.name in ('NRT_incref', 'NRT_decref'):
            self.marked.add(instr)


def _rewrite_function(function):
    # Mark NRT usage
    markpass = _MarkNrtCallVisitor()
    markpass.visit_Function(function)
    marked = markpass.marked
    # Remove NRT usage
    for bb in function.basic_blocks:
        for inst in list(bb.instructions):
            if inst in marked:
                bb.instructions.remove(inst)


_accepted_nrtfns = 'NRT_incref', 'NRT_decref'


def _legalize(module, dmm, fndesc):
    """
    Legalize the code in the module.
    Returns True if the module is legal for the rewrite pass that remove
    unnecessary refcount.
    """

    def valid_output(ty):
        """
        Valid output are any type that does not need refcount
        """
        model = dmm[ty]
        return not model.contains_nrt_meminfo()

    def valid_input(ty):
        """
        Valid input are any type that does not need refcount except Array.
        """
        return valid_output(ty) or isinstance(ty, types.Array)

    argtypes = fndesc.argtypes
    restype = fndesc.restype
    calltypes = fndesc.calltypes

    # Legalize function arguments
    for argty in argtypes:
        if not valid_input(argty):
            return False

    # Legalize function return
    if not valid_output(restype):
        return False

    # Legalize all called functions
    for callty in calltypes.values():
        if callty is not None and not valid_output(callty.return_type):
            return False

    # Ensure no allocation
    for fn in module.functions:
        if fn.name.startswith("NRT_"):
            if fn.name not in _accepted_nrtfns:
                return False

    return True


def remove_unnecessary_nrt_usage(function, context, fndesc):
    """
    Remove unnecessary NRT incref/decref in the given LLVM function.
    It uses highlevel type info to determine if the function does not need NRT.
    Such a function does not:

    - return array object;
    - take arguments that need refcount except array;
    - call function that return refcounted object.

    In effect, the function will not capture or create references that extend
    the lifetime of any refcounted objects beyound the lifetime of the
    function.

    The rewrite performs inplace.
    If rewrite has happen, this function return True. Otherwise, return False.
    """
    dmm = context.data_model_manager
    if _legalize(function.module, dmm, fndesc):
        _rewrite_function(function)
        return True
    else:
        return False

