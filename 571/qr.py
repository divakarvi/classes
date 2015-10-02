#! /usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

def cgs(A):
    assert isinstance(A, np.ndarray)
    assert A.ndim == 2
    m, n = A.shape
    assert m >= n
    Q = np.zeros((m,n))
    R = np.zeros((n,n))
    
    for i in range(n):
        col = np.array(A[:,i])
        Q[:, i] = col
        for j in range(i):
            qj = Q[:, j]
            dot = np.dot(col, qj)
            R[j, i] = dot
            Q[:,i] = Q[:, i] - dot * qj
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] = Q[:,i]/R[i, i]
    
    return Q, R
        
def mgs(A):
    assert isinstance(A, np.ndarray)
    assert A.ndim == 2
    m, n = A.shape
    assert m >= n
    Q = np.zeros((m,n))
    R = np.zeros((n,n))
    
    for i in range(n):
        col = np.array(A[:,i])
        Q[:, i] = col
        for j in range(i):
            qj = Q[:, j]
            dot = np.dot(col, qj)
            R[j, i] = dot
            col = col - dot * qj
        R[i, i] = np.linalg.norm(col)
        Q[:, i] = col/R[i, i]
    
    return Q, R

def mgsvscgs(n):
    A = np.random.randn(n, n)
    Q1, R1 = np.linalg.qr(A)
    A = np.random.randn(n, n)
    Q2, R2 = np.linalg.qr(A)
    D = np.diag(np.exp(np.array(range(-1,-n-1,-1))*1.0))
    A = np.dot(Q1, D)
    A = np.dot(A, Q2)
    
    Q, Rc = cgs(A)
    Q, Rm = mgs(A)
    Q, R = np.linalg.qr(A)
    
    plt.semilogy(abs(np.diag(Rc)),'ro', ms = 5.0)
    plt.semilogy(abs(np.diag(Rm)),'bo', ms = 5.0)
    plt.semilogy(abs(np.diag(R)),'go', ms = 5.0)
    plt.ylabel('magnitude of R(i,i)')
    plt.xlabel('i')
    plt.legend(['classical', 'modified', 'numpy'])
    plt.show()

def time(n):
    import time
    A = np.random.randn(n, n)
    tic = time.time()
    q, r = cgs(A)
    tc = time.time() - tic
    tic = time.time()
    q, r = mgs(A)
    tm = time.time() - tic
    tic = time.time()
    q, r = np.linalg.qr(A)
    tp = time.time() - tic
    return tc, tm, tp

def time_plot(ni, dn, n, cpughz):
    nlist = list(range(ni, n, dn))
    cycles = np.zeros((len(nlist), 3))
    for i, n in enumerate(nlist):
        tc, tm, tp = time(n)
        cycles[i, :] = np.array([tc, tm, tp])*cpughz*1e9/n/n/n/2.0
    print('cycles per flop for n = ', nlist[-1])
    print('cgs = '.rjust(30), cycles[-1,0])
    print('mgs = '.rjust(30), cycles[-1,1])
    print('numpy qr = '.rjust(30), cycles[-1,2])
    plt.plot(nlist, cycles[:,0], ':ok')
    plt.plot(nlist, cycles[:,1], '--ok')
    plt.plot(nlist, cycles[:,2], '-ok')
    plt.legend(['classical', 'modified', 'numpy'])
    plt.xlabel('n')
    plt.ylabel(r'$cycles/n^3$')
    plt.show()
    

def test_cgs(m = 100, n = 50):
    A = np.random.randn(m, n)
    Q, R = cgs(A)
    QR = np.dot(Q, R)
    print('error in A = '.rjust(30), np.linalg.norm(A-QR))
    diff = np.eye(n) - np.dot(Q.T, Q)
    print('error in Q = '.rjust(30), np.linalg.norm(diff))

def test_mgs(m = 100, n = 50):
    A = np.random.randn(m, n)
    Q, R = mgs(A)
    QR = np.dot(Q, R)
    print('error in A = ', np.linalg.norm(A-QR))
    diff = np.eye(n) - np.dot(Q.T, Q)
    print('error in Q = ', np.linalg.norm(diff))

if __name__ == '__main__':
    import textwrap, argparse
    description = textwrap.dedent(
    """
    mgs vs cgs for qr: accuracy, timing, testing
    """)
    parser = argparse.ArgumentParser(description=description, 
                                     prefix_chars = '+')
    parser.add_argument('+test',
                        action = 'store_true',
                        default = False,
                        help = 'test cgs and mgs')
    parser.add_argument('+time',
                        action = 'store_true',
                        default = False,
                        help = 'time cgs and mgs vs numpy qr')
    parser.add_argument('+ni',
                        type = int,
                        default = 100,
                        help = 'init n for timing (default 100)')
    parser.add_argument('+dn',
                        type = int,
                        default = 100,
                        help = 'increment in n for timing (default 100)')
    
    parser.add_argument('+accuracy',
                        action = 'store_true',
                        default = False,
                        help = 'compare accuracy of mgs and cgs')
    parser.add_argument('+cpughz',
                        type = float,
                        default = 3.3,
                        help = 'clock speed of cpu in gigahertz (default 3.3)')
    parser.add_argument('n', 
                        type = int,
                        help = 'n for testing/accuracy, final n for timing')
    args = parser.parse_args()
    
    if args.test:
        print('testing cgs ...')
        test_cgs(m = args.n, n = args.n)
        print('testing mgs ...')
        test_mgs(m = args.n, n = args.n)
        
    if args.time:
        assert args.n > args.ni and args.n - args.ni > args.dn
        time_plot(args.ni, args.dn, args.n, args.cpughz)

    if args.accuracy:
        mgsvscgs(n = args.n)
        
