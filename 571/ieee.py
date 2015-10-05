#!/usr/bin/env python
import numpy as np

def byte2int(c):
    if isinstance(c, str): #python2
        return ord(c)
    else: #python3
        return c


#from Dan Lecocq on stackexchange.com
def dblformat(num):
    import struct
    s = ''.join([bin(byte2int(c)).replace('0b', '').rjust(8, '0') 
                 for c in struct.pack('!d', num)])
    print(num,' -> ', s)
    print('       sign bit = ', s[0])
    print('  exponent bits = ', s[1:12])
    print(' precision bits = ', s[12:])
    print(' exponent value = ', int(s[1:12], 2))
    print('  effective exp = ', int(s[1:12],2)-1022)

def stdd1(x):
    assert isinstance(x, np.ndarray) and isinstance(x[0], float)
    ex = x.mean()
    exx = (x*x).mean()
    return np.sqrt(exx - ex**2)

def stdd2(x):
    assert isinstance(x, np.ndarray) and isinstance(x[0], float)
    ex = x.mean()
    x = x - ex
    return np.sqrt((x*x).mean())

def stdd_cmp(N):
    import numpy as np
    x = np.random.randn(N)
    print('variance of '+str(N)+' random numbers')
    print('   formula exx-ex**2 = '.rjust(50), stdd1(x))
    print('   formula e(x-ex)**2 = '.rjust(50), stdd1(x))
    print(' formula exx-ex**2 (1e8 added to all #s) = '.rjust(50), 
          stdd1(x + 1e8))
    print(' formula e(x-ex)**2 (1e8 added to all #s) = '.rjust(50), 
          stdd2(x + 1e8))

if __name__ == '__main__':
    import textwrap, argparse
    description = textwrap.dedent(
    """
    ieee double precision format, variance
    """)
    parser = argparse.ArgumentParser(description=description, 
                                     prefix_chars = '+')
    parser.add_argument('+double', 
                        action = 'store_true',
                        default = False,
                        help = 'print ieee storage format (default false)')
    parser.add_argument('+x',
                        type = float,
                        default = 0.0,
                        help = 'number whose format is printed (default 0.0)')
    parser.add_argument('+stdd', 
                        action = 'store_true',
                        default = False,
                        help = 'stadard dev using two formulas(default false)')
    parser.add_argument('+N',
                        type = int,
                        default = 10000,
                        help = 'N for checking stdd (default 10000)')
    args = parser.parse_args()
    
    if args.double:
        dblformat(args.x)

    if args.stdd:
        stdd_cmp(args.N)
        
