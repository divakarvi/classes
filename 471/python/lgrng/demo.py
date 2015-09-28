import numpy as np
import lgrng

def evalNinterp(f, x, xx):
    """\
    evalNinterp(f, x, xx):
    f = function being tested
    x = grid points
    xx = points for interpolation
    returns y, yy where y = f(x) and yy are interpolated at xx
    """
    assert isinstance(x, np.ndarray) and isinstance(xx, np.ndarray)
    
    y = np.empty(x.shape)
    for i,g in enumerate(x):
        y[i] = f(x[i])
        
    yy = lgrng.interp(x, y, xx)
    return y, yy

def demo(f, x, xx, showplot='yes'):
    """\
    plot(f, x, xx):
    f = function to be interpolated
    x = grid points
    xx = interpolation points
    plots interpolant and returns maximum error
    """
    from matplotlib import pyplot as plt
    y, yy = evalNinterp(f, x, xx)
    
    
    zz = np.zeros(xx.shape)
    for i,xp in enumerate(xx):
        zz[i] = f(xp)

    if(showplot == 'yes'):
        plt.plot(x, y, 'ro')
        plt.plot(xx, yy, 'k')
        plt.plot(xx, zz, 'b')
        plt.axis('tight')
        plt.xlabel('x')
        plt.ylabel('y')
        ax = plt.gca()
        #plt.text(0.4, 0.2, 'Error = '+str(error), 
        #     transform=ax.transAxes)
        plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])

    error = np.abs(zz - yy)
    error = np.max(error)
        
    
    return error


def unifvscheb(n):
    """\
    unifvscheb(n):
    graphs the function (x-x0)...(x-x_{n-1}) for unif and cheb
    point in [0,1].
    n must be even.
    functions nmlzed to be 1 at 0.
    """
    import gridpts as gr
    import numpy as np
    from matplotlib import pyplot as plt
    
    assert n%2 == 0
    x = gr.unif(n)
    xx = np.linspace(-1,1,200)*0.99+1e-6
    yy = gr.evalprod(x, xx)
    
    zero = np.array([0]) #nmlz
    yy = yy/gr.evalprod(x, zero)

    plt.subplot(211) 
    plt.plot(xx, yy)
    plt.title('nmlz prod poly with ' + str(n) + ' unif points')

    x = gr.cheb(n)
    yy = gr.evalprod(x, xx)
    
    yy = yy/gr.evalprod(x, zero) #nmlz

    
    plt.subplot(212) 
    plt.plot(xx, yy)
    plt.title('nmlz prod poly with ' + str(n) + ' cheb points')
