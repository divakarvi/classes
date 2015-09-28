from . import gridpts as gr
from . import demo
from . import hw2

def weights(x):
    """\
    weights(x): returns lgrng weights at grid points x
    entries of x assumed to be distinct
    """
    import numpy as np
    assert isinstance(x, np.ndarray)
    assert x.ndim == 1
    
    n, = x.shape
    w  = np.empty(n)
    
    for i in range(0,n):
        y = x[i] - x
        y[i] = 1.0
        w[i] = 1.0/np.prod(y)
    
    return w

def interp(x, y, xx, w = -1):
    """\
    interp(x, y, xx, w):
    x = grid points
    y = function values at x
    xx = points at which interpolant should be evaluated
    w = lgrng weights, -1 implies should be computed here
    returns interp values yy at xx
    """
    import numpy as np
    assert isinstance(x, np.ndarray) and isinstance(y, np.ndarray) \
         and isinstance(xx, np.ndarray)
    assert x.ndim == y.ndim == xx.ndim == 1

    if isinstance(w, int) and w == -1:
        w = weights(x)

    yy = np.empty(xx.shape)
    tmp = np.empty(x.shape)

    for i,g in enumerate(xx):
        tmp = g - x;
        fctr = np.prod(tmp)
        tmp = y*w*(1.0/tmp)
        yy[i] = fctr*np.sum(tmp)

    return yy
