import multiprocessing as mp
import numpy as np
import pyC

def pyc(a):
    nproc = mp.cpu_count()
    n = len(a)
    m = n*(n+1)/2
    b = np.zeros(m*nproc)
    
    pool = mp.Pool(nproc)
    for i in range(nproc):
        bi = b[i*m: (i+1)*m]
        pool.apply_async(pyC.tri_copy(a, n, bi))
    return b
    
