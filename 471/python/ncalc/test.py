import ncalc
from matplotlib import pyplot as plt
import numpy as np
from numpy import pi, sin, cos

def f1(x):
    return np.sqrt(1-x*x)

def f2(x):
    if x < 0:
        return 1+x
    else:
        return 1-np.sqrt(x)

def f(x):
    return sin(pi*x)

def df(x):
    return pi*cos(pi*x)

def ddf(x):
    return -pi*pi*sin(pi*x)

def eval():
    print('testing vectorized eval')
    x = np.linspace(-1, 1, 200)
    y = ncalc.eval(f1, x)
    plt.figure(1)
    plt.plot(x, y)
    plt.title('$y=\sqrt{1-x^2}$, vectorized evaluation')
    plt.figure(2)
    y = ncalc.eval(f2, x)
    plt.plot(x, y)
    plt.title('$y=1-|x|$ and $y=1-|\sqrt{x}|$, not vectorized')
    plt.show()

def diff():
    nlist = [101, 1001, 4001, 10001]
    h = np.zeros(len(nlist))
    fwd = np.zeros(len(nlist))
    cntrd = np.zeros(len(nlist))
    cntrdd = np.zeros(len(nlist))
    for i,n in enumerate(nlist):
        x = np.linspace(-1, 1, n)
        y = f(x)
        dy = df(x)
        ddy = ddf(x)
        
        h[i] = x[1] - x[0]
        dyf = ncalc.diff.fwd(y, h[i])
        dyc = ncalc.diff.cntrd(y, h[i])
        ddyc = ncalc.diff2.cntrd(y, h[i])
    
        fwd[i] = max(abs(dyf-dy[:-1])) 
        cntrd[i] = max(abs(dyc - dy[1:-1]))
        cntrdd[i] = max(abs(ddyc - ddy[1:-1]))
    
    plt.loglog(h, fwd, lw=2, c = 'k')
    plt.loglog(h, cntrd, ls='--', lw = 2, c = 'g')
    plt.loglog(h, cntrdd, ls='-.', lw = 2, c = 'b')
    plt.show()

def intg():
    nlist = [101, 1001, 4001, 10001]
    h = np.zeros(len(nlist))
    trpzm = np.zeros(len(nlist))
    simpson = np.zeros(len(nlist))
    for i,n in enumerate(nlist):
        x = np.linspace(0, 1, n)
        y = f(x)
        h[i] = x[1] - x[0]
        trpzm[i] = ncalc.intg.trpzm(y, h[i])
        trpzm[i] = abs(trpzm[i] - 2.0/pi)
        simpson[i] = ncalc.intg.simpson(y, h[i])
        simpson[i] = abs(simpson[i] - 2.0/pi)

    plt.loglog(h, trpzm, lw=2, c='k')
    plt.loglog(h, simpson, ls='--', lw=2, c='r')
    plt.show()
