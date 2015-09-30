#! /usr/bin/env python
def f(x, y):
    x = -7
    return x+y

def g(x, y):
    x[0] = 7
    return y

from matplotlib import pyplot as plt
import numpy as np



if __name__ == '__main__':
    x = np.linspace(0.0, 10.0, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
