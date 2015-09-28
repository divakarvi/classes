from __future__ import print_function

def form1(x):
    import numpy as np
    assert isinstance(x, np.ndarray) and isinstance(x[0], float)
    
    ex = x.mean()
    exx = (x*x).mean()
    return np.sqrt(exx - ex**2)

def form2(x):
    import numpy as np
    assert isinstance(x, np.ndarray) and isinstance(x[0], float)

    ex = x.mean()
    x = x - ex
    return np.sqrt((x*x).mean())

def demo():
    import numpy as np
    N = 10000
    x = np.random.randn(N)
    print('variance of '+str(N)+' random numbers')
    print('   formula 1 = ', form1(x))
    print('   formula 2 = ', form2(x))
    print(' formula 1 (1e8 added to all #s) = ', form1(x + 1e8))
    print(' formula 2 (1e8 added to all #s) = ', form2(x + 1e8))
