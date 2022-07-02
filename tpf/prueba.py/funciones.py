def constant(t):
    result = 1
    
def linear(t,t0):
    result = t / t0
    
def invlinear(t, t0):
    if (1 - t/t0) < 0:
        answer = 0
    elif (1 - (t/t0)) >= 0:
        result = 0