def trpzm(y,h):
    return h*(0.5*y[0] + sum(y[1:-1]) + 0.5*y[-1])

def simpson(y, h):
    assert len(y)%2==1
    return h/3.0*(y[0]
		  + 4.0*sum(y[1:-1:2])
		  + 2.0*sum(y[2:-2:2])
		  + y[-1])
    
