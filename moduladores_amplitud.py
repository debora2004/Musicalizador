import math

class mod_amp:
    def __init__(self, attack, sustain, decain):
        self.attack = attack.lower()
        self.sustain = sustain.lower()
        self.decain = decain.lower()
    
    def constant(self, t):
        result = 1
        return result
        
    def linear(self, t, t0):
        result = t / t0
        return result
        
    def invlinear(self, t, t0):
        if (1 - t/t0) < 0:
            result = 0
        elif (1 - (t/t0)) >= 0:
            result = 0
        return result

    def sin(self, t, a, f):
        result = 1 + (a * math.sin(f*t))    
        return result
        
    def exp(self, t, t0):
        result = math.exp((5*(t-t0))/t0)
        return result

    def invexp(self, t, t0):
        result = math.exp((-5*t)/t0)
        return result
        
    def quartcos(self, t, t0):
        result = math.cos(((math.pi)*t)/(2*t0))
        return result
        
    def quartsin(self, t, t0):
        result = math.sin(((math.pi)*t)/(2*t0))
        return result
        
    def halfcos(self, t, t0):
        result = (1 + math.cos((math.pi*t)/t0))/2
        return result

    def halfsin(self, t, t0):
        result = (1 + math.cos(math.pi*((t/t0)-(1/2))))/2
        return result

    def log(self, t, t0):
        result = math.log10(((9*t)/t0) + 1)
        return result

    def invlog(self, t, t0):
        if t < t0:
            result = math.log10(((-9*t)/t0) + 10)
        elif t >= t0:
            result = 0
        return result

    def tri(self, t, t0, t1, a1):
        if t < t1:
            result = (t*a1)/t1
        elif t > t1:
            result = ((t-t1)/(t1-t0)) + a1
        return result

    def pulses(self, t, t0, t1, a1):
        """ 
        t_prima = t/t0 - mod(t/t0)
        f(t_prima) = min{ mod(((1-a1)/t1)*(t_prima - t0 + t1)) + a1}
        """