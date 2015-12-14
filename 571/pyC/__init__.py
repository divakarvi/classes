import os, ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

tri_copy = None
dblptr = ndpointer(ctypes.c_double, flags='C_CONTIGUOUS')

def init():
    """
    initializes tri_copy to function in tri_copy.so
    """
    global tri_copy
    if os.path.isabs(__file__):
        print('abs path name')
        i = __file__.find(r'/__init__.py')
        fname = os.path.join(__file__[:i], 'tri_copy.so')
        print('loading ... ', fname)
    else:
        i = __file__.find(r'__init__.py')
        print('not abs path name')
        fname = os.path.join(os.path.abspath('.'),__file__[:i], 'tri_copy.so')
        print('loading ... ', fname)
    triso = ctypes.cdll.LoadLibrary(fname)
    tri_copy = triso.tri_copy
    tri_copy.restype = None
    tri_copy.argtypes = [dblptr, ctypes.c_int, dblptr]
############################################################
init() 
############################################################
