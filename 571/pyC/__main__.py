import numpy as np
import pyC

def test(n):
    a = np.array(range(n))*1.0
    b = np.zeros(n*(n+1)/2)
    pyC.tri_copy(a, n, b)
    print('a = '.rjust(10), a)
    print('b = '.rjust(10))
    for i in range(n):
        print(''.rjust(10), b[i*(i+1)/2:i*(i+1)/2+i+1])


def pycopy(a, b):
    n = len(a)
    assert len(b) == n*(n+1)/2
    for i in range(n):
        b[i*(i+1)/2:i*(i+1)/2+i+1] = a[i]

def pyccopy(a, b):
    n = len(a)
    assert len(b) == n*(n+1)/2
    for i in range(n):
        for j in range(i+1):
            b[i*(i+1)/2+j] = a[i]

def timer(n, ntrials):
    import time
    secs = np.zeros((ntrials, 3))
    b = np.zeros(n*(n+1)/2)
    for i in range(ntrials):
        a = np.random.randn(n)

        init = time.time()
        pyC.tri_copy(a, n, b)
        secs[i,0] = time.time() - init

        init = time.time()
        pycopy(a, b)
        secs[i, 1] = time.time() - init

        init = time.time()
        pyccopy(a, b)
        secs[i, 2] = time.time() - init
    
    print('n = '.rjust(25), n)
    print('ntrials = '.rjust(25), ntrials)
    print('------------'.rjust(30))
    print('median times'.rjust(30))
    print('------------'.rjust(30))
    print('plain  C = '.rjust(25), 
          '{0:.2e}'.format(np.median(secs[:,0])), ' s')
    print('py with slices = '.rjust(25), 
          '{0:.2e}'.format(np.median(secs[:,1])), ' s')
    print('py without slices  = '.rjust(25), 
          '{0:.2e}'.format(np.median(secs[:,2])), ' s')

if __name__ == '__main__':
    import textwrap, argparse
    description = textwrap.dedent(
    """
    time/test triangular copy
    a, b, c, ... -> a, b, b, c, c, c, ...
    """)
    parser = argparse.ArgumentParser(description=description, 
                                     prefix_chars = '+')
    parser.add_argument('+test', 
                        action = 'store_true',
                        default = False,
                        help = 'test triangular copy')
    parser.add_argument('+time', 
                        action = 'store_true',
                        default = False,
                        help = 'time triangular copy in C and python')
    parser.add_argument('+ntrials', 
                        type = int,
                        default = 10,
                        help = 'number of trials for timing')
    parser.add_argument('n',
                        type = int,
                        help = 'n for testing/timing')
    args = parser.parse_args()
    
    if args.test:
        test(args.n)

    if args.time:
        timer(args.n, args.ntrials)
