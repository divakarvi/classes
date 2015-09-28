def fwd(y, h):
    dy = (y[1:] - y[:-1])/h
    return dy

def cntrd(y, h):
    dy = (y[2:]-y[:-2])/(2.0*h)
    return dy

def cntrdxx(y, h):
    a = 1.0/12
    b = -2.0/3
    c = 0
    d = 2.0/3
    e = -1.0/12
 
    dy = a*y[:-4] + b*y[1:-3] + d*y[3:-1] + e*y[4:]
    return dy/(h)
