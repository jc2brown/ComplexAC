import Complex


class MathFunc:
    
    l = None
    
    def __init__(self, l):
        self.l = l
        
    def __add__(self, f):
        return MathFunc( lambda x: self(x) + f(x) )  
    
    def __sub__(self, f):
        return MathFunc( lambda x: self(x) - f(x) )
        
    def __mul__(self, f):
        return MathFunc( lambda x: self(x) * f(x) )
    
    def __div__(self, f):
        return MathFunc( lambda x: self(x) / f(x) )  
    
    def __call__(self, x):
        return self.l(x)
    