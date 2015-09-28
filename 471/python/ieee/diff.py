import ncalc

def errorf(f, df, x, h):
    """\
    error(f, df, x, h): 
    find error in df computed using fwd differences at x
    return error (h = const intvl spacing)
    """
    import numpy as np
    xx = np.array([x, x+h], dtype=float)
    
    y = f(xx)
    dy = df(x)
    dyf = ncalc.diff.fwd(y, h)[0]
    err = abs(dy-dyf)
    return err

def demo():
    nlist = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9,
         10**10, 10**11, 10**12, 10**13, 10**14, 10**15]
         
    l = len(nlist)
    import numpy as np
    err = np.empty(l)
    h = np.empty(l)
    
    from ncalc.test import f #sin(pi*x)
    from ncalc.test import df #pi*cos(pi*x)
    x = 1.2
    for i,n in enumerate(nlist):
        h[i] = 1.0/n
        err[i] = errorf(f, df, x, h[i])

    from matplotlib import pyplot as plt
    plt.loglog(h, err)
    plt.xlabel('h')
    plt.ylabel('error in fwd difference')
    plt.title('x = '+str(x))
