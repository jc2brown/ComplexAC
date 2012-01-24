
from Complex import *
from MathFunc import *

class Passive(object):
    # some parameter
    p = 0
    
    def __init__(self, p):
        self.p = p
    
    def V(self, I):
        return MathFunc( lambda w: I(w) * self.Z()(w) )
    
    def I(self, V):
        return MathFunc( lambda w: V(w) / self.Z()(w) )
        
class Res(Passive):
    def Z(self):
        return MathFunc( lambda w: polar(self.p, 0) )

class Cap(Passive):    
    def Z(self):
        return MathFunc( lambda w: polar(1/(w*self.p), -90) )
    
class Ind(Passive):
    def Z(self):
        return MathFunc( lambda w: polar(w*self.p, 90) )

