def cntrd(y, h):
    ddy = (y[:-2] - 2*y[1:-1] + y[2:])/(h*h)
    return ddy
