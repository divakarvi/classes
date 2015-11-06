import numpy as np
from matplotlib import pyplot as plt

def ptinbox(axes, center, zoom = 1.25):
    dim = len(axes)
    assert len(center) == dim
    x = np.zeros(dim)
    for i in range(dim):
        low = center[i] - axes[i]*zoom
        high = center[i] + axes[i]*zoom
        x[i] = np.random.uniform(low = low, high = high)
    return x

def ptsinbox(n, axes, center, zoom = 1.25):
    dim = len(axes)
    assert len(center) == dim
    x = np.zeros((n,dim))
    for i in range(dim):
        low = center[i] - axes[i]*zoom
        high = center[i] + axes[i]*zoom
        x[:,i] = np.random.uniform(low = low, high = high, size = n) 
    return x

class Ellipse:
    def __init__(self, axes = (1.0, 1.0), center = (0.0, 0.0)):
        assert isinstance(axes, tuple)
        assert isinstance(center, tuple) and len(center) == len(axes)
        self.axes = axes
        self.center = center
        
    def samples(self, n, epsilon = 0.01, zoom = 1.25):
        assert epsilon < .75 and epsilon >= 0
        axes = self.axes
        center = self.center
        dim = len(axes)
        
        def margin(x):
            """
            margin in/out of ellipse
            """
            s = 0.0
            for i in range(len(axes)):
                s = s + (x[i]-center[i])**2/axes[i]**2
            return s - 1.0
    
        m = 2*n
        nvalid = 0
        while nvalid < n:
            pts = ptsinbox(m, axes = axes, center = center, zoom = zoom)
            nvalid = 0
            for i in range(m):
                if abs(margin(pts[i,:])) > epsilon:
                    nvalid = nvalid + 1
            m = 2*m
    
        x = np.zeros((n, dim))
        y = np.zeros(n)
        frm = 0
        for i in range(n):
            while abs(margin(pts[frm,:])) < epsilon:
                frm = frm + 1
            x[i,:] = pts[frm, :]
            y[i] = margin(x[i,:])
            frm = frm + 1
            
        return x, y
        
    def featurize(self, pts):
        n, dim = pts.shape
        assert dim == 2
        xx = np.zeros((n,6))
        for i in range(n):
            x = pts[i,0]
            y = pts[i, 1]
            xx[i,:] = [x**2, x*y, y**2, x, y, 1]
        return xx

    def plot(self):
        axes = self.axes
        center = self.center
        t = np.linspace(0.0, 2*np.pi, 200)
        plt.plot(axes[0]*np.cos(t) + center[0], 
                 axes[1]*np.sin(t) + center[1], 
                 '-k', lw = 3.5)


def rosen(xx, y, maxiter = 10, tol = 0.1):

    def update(w, x, y):
        if np.dot(w,x)*y > 0:
            return 'ok'
        else:
            w[:] = w + y*x
            return 'fixed'
            
    n, dim = xx.shape
    w = np.zeros(dim)
    niter = 0
    while niter < maxiter:
        miscl = 0
        for i in range(n):
            ans = update(w, xx[i,:], y[i])
            if ans == 'fixed':
                miscl += 1
        print(miscl/n)
        if miscl/n <= tol:
            return w
        niter += 1
    return w


def graphw(w, xmin = -5.0, xmax = 5.0):

    def x2y(x, w):
        """
        w is x**2, xy, y**2, x, y, 1
        """
        a = w[2]
        b = w[1]*x + w[4]
        c = w[0]*x**2 + w[3]*x + w[5]
        if b*b - 4*a*c < 0:
            return None
        else:
            return np.roots([a,b,c]).real

    xarr = np.linspace(xmin, xmax, 1000)
    xs = []
    ys = []
    for x in xarr:
        y = x2y(x, w)
        if isinstance(y, np.ndarray):
            for yy in y:
                xs.append(x)
                ys.append(yy)
    plt.plot(xs, ys, 'ro')
        

if __name__ == '__main__':
    e = Ellipse(axes = (3.0,2.0), center = (1.0, 1.0))
    e.plot()
    x, y = e.samples(1000, 0.02)
    xx = e.featurize(x)
    w = rosen(xx, y, maxiter = 10, tol = 0.01)
    graphw(w, xmin = -10.0, xmax = 10.0)
    plt.plot(x[:,0], x[:,1], 'o')
    plt.axis('equal')
    plt.show()
