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

def time_plot(n, cpughz = 3.3):
    nlist = list(range(200, n, 100))
    cycles = np.zeros((len(nlist), 3))
    for i, n in enumerate(nlist):
        tc, tm, tp = time(n)
        cycles[i, :] = np.array([tc, tm, tp])*cpughz*1e9/n/n/n
    print(cycles[-1,:])
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
    print('error in A = ', np.linalg.norm(A-QR))
    diff = np.eye(n) - np.dot(Q.T, Q)
    print('error in Q = ', np.linalg.norm(diff))

def test_mgs(m = 100, n = 50):
    A = np.random.randn(m, n)
    Q, R = mgs(A)
    QR = np.dot(Q, R)
    print('error in A = ', np.linalg.norm(A-QR))
    diff = np.eye(n) - np.dot(Q.T, Q)
    print('error in Q = ', np.linalg.norm(diff))

if __name__ == '__main__':
    #test_cgs(1000, 500)
    #test_mgs(1000, 500)
    #mgsvscgs(100);
    time_plot(1000)
