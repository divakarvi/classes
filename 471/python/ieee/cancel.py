from __future__ import print_function

def demo(x, y):
    print('x = '.rjust(16,' '), '{0:.16f}'.format(x))
    print('y = '.rjust(16,' '), '{0:.16f}'.format(y))

    import numpy as np
    shift = np.arange(0, 25)
    shift = 10.0**shift

    for s in shift:
        print()
        diff = (x+s) - (y+s)
        print('(x+s)-(y+s) = '.rjust(16,' '), '{0:.16f}'.format(diff), 
              's = '.rjust(6,' '), '{0:.3e}'.format(s))
