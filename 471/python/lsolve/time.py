from __future__ import absolute_import
from __future__ import print_function

def time_solve(n):
    assert isinstance(n, int)
    import time
    import numpy as np
    from numpy import random
    from scipy import linalg
    from time import time
    A = random.randn(n, n)
    b = random.randn(n, 1)
    
    count = 3
    secs = np.zeros(count)
    flopr = np.zeros(count)

    for i in range(count):
        a = time()
        x = linalg.solve(A, b)
        c = time()
        secs[i] = c - a
        flopr[i] = 2.0*n*n*n/3.0/secs[i]

    import gc
    gc.collect()
    return np.median(secs), np.median(flopr)


def plot(n1 = 100, n2 = 2000):
    import numpy as np
    nlist = np.linspace(n1, n2, 5)
    nlist = nlist.astype(int)
    secs = np.empty(nlist.shape)
    flopr = np.empty(nlist.shape)

    for i,n in enumerate(nlist):
        secs[i], flopr[i] = time_solve(n)

    from matplotlib import pyplot as plt
    plt.loglog(nlist, secs)
    plt.loglog(nlist, secs, 'ro', ms=5)
    plt.xlabel('N')
    plt.ylabel('Seconds')
    plt.show()

    plt.figure()
    plt.plot(nlist, flopr)
    plt.plot(nlist, flopr, 'ko', ms=5)
    plt.xlabel('N')
    plt.ylabel('Gigaflops/sec')
    plt.show()

