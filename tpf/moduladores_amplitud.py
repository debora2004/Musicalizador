import math

class Moduladores_amplitud:
    def __init__(self, function, parameters, types):
        self.types = types
        function = function.lower()
        self.result = self.function
        
    def constant(self, t):
        if self.types == 'sustain':
            result = 1
            return result
        else: 
            raise ArithmeticError
        
    def linear(self, t, t0):
        if self.types == 'attack':
           result = t / t0
           return result
        else: 
            raise ArithmeticError

        
    def invlinear(self, t, t0):
        if self.types == 'sustain' or self.types == 'decay':
            if (1 - t/t0) < 0:
                result = 0
            elif (1 - (t/t0)) >= 0:
                result = 0
            return result
        else: 
            raise ArithmeticError


    def sin(self, t, a, f):
        if self.types == 'sustain':
            result = 1 + (a * math.sin(f*t))    
            return result
        else: 
            raise ArithmeticError

        
    def exp(self, t, t0):
        if self.types == 'attack':
            result = math.exp((5*(t-t0))/t0)
            return result
        else: 
            raise ArithmeticError


    def invexp(self, t, t0):
        if self.types == 'sustain' or self.types == 'decay':     
            result = math.exp((-5*t)/t0)
            return result
        else: 
            raise ArithmeticError

        
    def quartcos(self, t, t0):
        if self.types == 'sustain' or self.types == 'decay':
            result = math.cos(((math.pi)*t)/(2*t0))
            return result
        else: 
            raise ArithmeticError

        
    def quartsin(self, t, t0):
        if self.types == 'attack':
            result = math.sin(((math.pi)*t)/(2*t0))
            return result
        else: 
            raise ArithmeticError

        
    def halfcos(self, t, t0):
        if self.types == 'sustain' or self.types == 'decay':
            result = (1 + math.cos((math.pi*t)/t0))/2
            return result
        else: 
            raise ArithmeticError


    def halfsin(self, t, t0):
        if self.types == 'attack':
            result = (1 + math.cos(math.pi*((t/t0)-(1/2))))/2
            return result
        else: 
            raise ArithmeticError


    def log(self, t, t0):
        if self.types == 'attaack':
            result = math.log10(((9*t)/t0) + 1)
            return result
        else: 
            raise ArithmeticError


    def invlog(self, t, t0):
        if self.types == 'sustain' or self.types == 'decay':   
            if t < t0:
                result = math.log10(((-9*t)/t0) + 10)
            elif t >= t0:
                result = 0
            return result
        else: 
            raise ArithmeticError


    def tri(self, t, t0, t1, a1):
        if self.types == 'attack':
            if t < t1:
                result = (t*a1)/t1
            elif t > t1:
                result = ((t-t1)/(t1-t0)) + a1
            return result
        else: 
            raise ArithmeticError


    def pulses(self, t, t0, t1, a1):
        # sustain
        if self.types == 'sustain':
            pass
        else: 
            raise ArithmeticError

        """ 
        t_prima = t/t0 - mod(t/t0)
        f(t_prima) = min{ mod(((1-a1)/t1)*(t_prima - t0 + t1)) + a1}
        """
        
a = Moduladores_amplitud('EXP', (0.2), )



