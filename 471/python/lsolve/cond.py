def randm(n):
    from numpy import random
    A = random.randn(n,n)
    return A

def laplace(n):
    import numpy as np
    A = np.zeros([n, n])
    np.fill_diagonal(A, 2.0)
    for i in range(n-1):
        A[i+1, i] = -1.0
        A[i, i+1] = -1.0
    return A
    

def makeplot(nmax, flag):
    assert flag=='rand' or flag=='hilb' or flag=='laplace'
    from scipy import linalg
    import numpy as np
    from matplotlib import pyplot as plt

    if flag == 'rand':
        getmtrx = randm
        plotf = plt.loglog
    elif flag == 'hilb':
        getmtrx = linalg.hilbert
        plotf = plt.semilogy
    else:
        assert flag=='laplace'
        getmtrx = laplace
        plotf = plt.loglog

    nlist = np.linspace(25, nmax, 6)
    nlist = nlist.astype(int)
    clist = np.empty(len(nlist))

    for i,n in enumerate(nlist):
        A = getmtrx(n)
        clist[i] = np.linalg.cond(A)
        

    plotf(nlist, clist)
    plotf(nlist, clist, 'ro', ms = 4) 

def plot():
    from matplotlib import pyplot as plt
    plt.figure(1)
    makeplot(nmax = 1000, flag = 'rand')
    plt.title('Condition number vs. n for random matrix')
    plt.xlabel('N', fontsize = 16)
    plt.ylabel('$\kappa(A)$', fontsize = 16)
    plt.show() 

    plt.figure(2)
    makeplot(nmax = 150, flag = 'hilb')
    plt.title('Condition number vs. n for hilbert matrix')
    plt.xlabel('N', fontsize = 16)
    plt.ylabel('$\kappa(A)$', fontsize = 16)
    plt.show()

    plt.figure(3)
    makeplot(nmax = 1000, flag = 'laplace')
    plt.title('Condition number vs. n for discrete Laplacian')
    plt.xlabel('N', fontsize = 16)
    plt.ylabel('$\kappa(A)$', fontsize = 16)
    plt.show()
