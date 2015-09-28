import ncalc

def pblm3():
    import numpy as np
 
    def f(x):
        from numpy import exp, sin, pi
        return exp(sin(pi*x))
 
    def df(x):
        from numpy import exp, cos, pi
        return pi*cos(pi*x)*f(x)
 
    def error(a, b, n):
        x = np.linspace(a, b, n+1)
        h = x[1] - x[0]
       
        y = f(x)
        dy = df(x)[2:-2]
       
        dyc = ncalc.diff.cntrdxx(y, h)
        err = max(abs(dyc - dy))
 
        return h, err
 
    a = 0
    b = 1
    nlist = [10, 10**2, 5*10**2, 8*10**2, 10**3]
    h = np.zeros(len(nlist))
    err = np.zeros(h.shape)
 
    for i, n in enumerate(nlist):
        h[i], err[i] = error(a, b, n)
 
    from matplotlib import pyplot as plt
    plt.loglog(h, err)

def pblm7():
    import numpy as np
    
    def f(x):
        return np.exp(x)

    def int_f(x):
        return np.exp(x)

    def error(a, b, n):
        assert n%2 == 0
        x = np.linspace(a, b, n+1)
        h = x[1] - x[0]
        y = f(x)
        ans = ncalc.intg.simpson(y, h)
        error = abs(int_f(b) - int_f(a) - ans)
        return h, error
        
    nlist = [2*10, 2*100, 2*200, 2*400, 2*800]
    h = np.zeros(len(nlist))
    err = np.zeros(len(nlist))

    for i, n in enumerate(nlist):
        h[i], err[i] = error(-1, 1, n)

    from matplotlib import pyplot as plt
    plt.loglog(h, err)
