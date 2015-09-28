#! /usr/bin/env python
import numpy as np

def proj_out(a, q):
    assert isinstance(a, np.ndarray)
    assert isinstance(q, np.ndarray)
    assert a.ndim == q.ndim and a.ndim == 1 and a.shape == q.shape
    dot = np.dot(a, q)
    ap = a - dot*q
    return ap, dot


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
        
        
    

def test_projout():
    a = np.linspace(1.0, 4.0, 4)
    q = np.ones(4)
    q = q/np.linalg.norm(q)
    ap, dot = proj_out(a, q)
    print(q)
    print(a)
    print(ap)

def test_qr(m = 100, n = 50):
    A = np.random.randn(m, n)
    Q, R = cgs(A)
    QR = np.dot(Q, R)
    print('error in A = ', np.linalg.norm(A-QR))
    diff = np.eye(n) - np.dot(Q.T, Q)
    print('error in Q = ', np.linalg.norm(diff))

if __name__ == '__main__':
    #test_projout()
    test_qr(1000, 500)
