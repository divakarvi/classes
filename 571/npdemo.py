#!/usr/bin/env python
import numpy as np

#constructors in numpy
a = np.zeros((5,6))
print(a)
b = np.ones((3,4))
print(a)
c = np.random.randn(4,5)
print(c)
d = np.array([[1,4,7], [23,5,6]])
print(d)

#aliasing (everthing a pointer except basic types)
aa = a
aa[1,1] = 1111
print(a)

#making copies of matrices
aa = np.array(a)
aa[1,1] = 2222
print(a)

aa = np.copy(a)
aa[1,1] = 0
print(a)

#slicing matrices
print(d)
dsub = d[1:, 0:2]

#some of the parameters of numpy arrays
print(d.dtype)
print(d.ndim)
print(d.shape)
d = d*1.0
print(d.dtype)
print(d)

#making basic plots
x = np.linspace(0.0, 10.0, 200)
y = np.sin(x)
from matplotlib import pyplot as plt
p1, = plt.plot(x, y, '-k')
plt.plot(x[::10], y[::10], 'ob', ms = 5)
p2, = plt.plot(x, np.cos(x), '--r')
plt.legend([p1, p2], ['sin', 'cos'])
plt.xlabel('x')
plt.show()
