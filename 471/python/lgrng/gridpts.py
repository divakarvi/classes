import numpy as np

def unif(n):
    """\
    unif(n): returns n grid pts uniformly spaced in [-1, 1]
    """
    x = np.linspace(-1.0, 1.0, n)
    return x

def cheb(n):
    """\
    cheb(n): returns n cheb pts uniformly spaced in [-1, 1]
    """
    x = np.linspace(0, np.pi, n)
    return np.cos(x)
    
def evalprod(x, xx):
    """\
    evalprod(x, xx):
    returns yy
    yy[i] = prod(xx[i] - x[j]) over j  
    """
    yy = np.empty(xx.shape)
    for i in range(len(xx)):
        dx = xx[i] - x
        yy[i] = np.prod(dx)
    
    return yy
