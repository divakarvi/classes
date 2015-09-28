def demo(f, x, xx, kind = 3):
    """\
    f = function to be interpolated
    x = grid points
    xx = interpolation points
    kind = order of spline
    plots fn and interpolant
    """
    from scipy import interpolate 
    from matplotlib import pyplot as plt
    import numpy as np
    
    y = np.empty(x.shape)
    y = f(x)
        
    ff = interpolate.interp1d(x, y, kind=kind)
    yy = ff(xx)
    zz = f(xx)
    error = max(abs(zz-yy))

    plt.plot(x, y, 'ro')
    plt.plot(xx, yy, 'k')
    ax = plt.gca()
    plt.text(0.3, 0.2, 'error = '+str(error), 
         transform = ax.transAxes)
    
if __name__ == '__main__':
    import numpy as np
    import scipy as sp
    from scipy import interpolate
    from matplotlib import pyplot as plt
    import lgrng
    
    x = np.linspace(0, np.pi, 20)
    xx = np.linspace(0, np.pi, 2000)
    demo(np.sin, x, xx)
    plt.axis('tight')
    plt.show()
