from __future__ import print_function

def showerr(A, x):
    import numpy as np
    b = np.dot(A,x)

    from scipy import linalg
    xx = linalg.solve(A, b)

    fwd_err = linalg.norm(x-xx)/linalg.norm(x)
    res_err = linalg.norm(b - np.dot(A,xx))/linalg.norm(b)
    print('               cond # = ', np.linalg.cond(A))
    print('              res_err = ', res_err)
    print('              fwd_err = ', fwd_err)

    Ainv = linalg.inv(A)
    xx = np.dot(Ainv, b)
    
    fwd_err = linalg.norm(x-xx)/linalg.norm(x)
    res_err = linalg.norm(b - np.dot(A,xx))/linalg.norm(b)
    print('res_err using inverse = ', res_err)
    print('fwd_err using inverse = ', fwd_err)



def demo(n):
    from numpy import random
    from scipy import linalg
    A = random.randn(n, n)
    x = random.randn(n)
    
    print('\n\t\t Random matrix of dimension', n)
    showerr(A, x)

    A = linalg.hilbert(n)
    print('\n\t\t Hilbert matrix of dimension', n)
    showerr(A, x)

    from . import cond
    A = cond.laplace(n)
    print('\n\t\t Disc Laplacian of dimension', n)
    showerr(A, x)
