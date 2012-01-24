import Complex

class MathFunc:
    l = None
    def __init__(self, l):
        self.l = l
        
    def __add__(self, f):
        if f.__class__ is Complex.Complex:
            return MathFunc( lambda x: self.l(x) + f )
        return MathFunc( lambda x: self.l(x) + f(x) )  
    
    def __sub__(self, f):
        if f.__class__ is Complex.Complex:
            return MathFunc( lambda x: self.l(x) - f )
        return MathFunc( lambda x: self.l(x) - f(x) )  
        
    def __mul__(self, f):
        if f.__class__ is Complex.Complex:
            return MathFunc( lambda x: self.l(x) * f )
        return MathFunc( lambda x: self.l(x) * f(x) )
    
    def __div__(self, f):
        if f.__class__ is Complex.Complex:
            return MathFunc( lambda x: self.l(x) / f )
        return MathFunc( lambda x: self.l(x) / f(x) )  
    
    def __call__(self, x):
        return self.l(x)
    