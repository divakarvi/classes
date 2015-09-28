
def errors(f, a, b, n, I):
    import ncalc
    import numpy as np
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = x[1] - x[0]
    Ia = ncalc.intg.simpson(y, h)
    return h, abs(I-Ia)

def demo():
    def f(x):
        return 1/(1+x**2)
    
    a = 0
    b = 1
    nlist = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]
    import numpy as np
    I = np.pi/4.0
    h = np.empty(len(nlist))
    err = np.empty(len(nlist))
    
    for i,n in enumerate(nlist):
        h[i], err[i] = errors(f, a, b, n, I)
        import gc
        gc.collect()

    from matplotlib import pyplot as plt
    plt.loglog(h, err)
    plt.xlabel('h for Simpson rule', fontsize = 16)
    plt.ylabel('error', fontsize = 16)
    
