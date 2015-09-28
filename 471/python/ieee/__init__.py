from __future__ import print_function
from . import diff
from . import cancel
from . import intg
from . import stdd

def byte2int(c):
    if isinstance(c, str): #python2
        return ord(c)
    else: #python3
        return c


#from Dan Lecocq on stackexchange.com
def binary(num):
    import struct
    s = ''.join([bin(byte2int(c)).replace('0b', '').rjust(8, '0') 
		     for c in struct.pack('!d', num)])
    print(num,' -> ', s)
    print('       sign bit = ', s[0])
    print('  exponent bits = ', s[1:12])
    print(' precision bits = ', s[12:],'\n')
    print(' exponent value = ', int(s[1:12], 2))
    print('  effective exp = ', int(s[1:12],2)-1023)
