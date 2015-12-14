import numpy as np
from . import pyc
import multi

def sumcopy(a):
    b = pyc.pyc(a)
    s = multi.mysum(b)
    return s, b
