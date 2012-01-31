
from Complex import *
from MathFunc import *

class Passive(object):
    # some parameter
    p = None
    z = None
    
    def __init__(self, p):
        self.p = p
                    
    def setImp(self, z):
        self.z = z
    
    def V(self, I):
        if ( self.z is not None):
            return I * self.z
        return MathFunc( lambda w: I(w) * self.Z()(w) )
    
    def I(self, V):
        if ( self.z is not None):
            return V / self.z
        return MathFunc( lambda w: V(w) / self.Z()(w) )
        
class Res(Passive):
    def Z(self):
        return Polar(self.p, 0)

class Cap(Passive):
    def setReac(self, x):
        self.z = Polar(x, -90)
        return self
    def Z(self):
        if ( self.z is not None):
            return self.z
        return MathFunc( lambda w: Polar(1/(w*self.p), -90) )
        
class Ind(Passive):
    def setReac(self, x):
        self.z = Polar(x, 90)
        return self
    def Z(self):
        if ( self.z is not None):
            return self.z
        return MathFunc( lambda w: Polar(w*self.p, 90) )

#class Load(Passive):
#    real = None
#    reac = None
#    app = None
#    def setReac(self, x):
#        self.reac = x
#        recal()  
#        return self
#    def setReal(self, x):
#        self.real = Polar(x, 0)
#        return self
#    def recal(self):
#        
#    def Z(self):
#        if ( self.z is not None):
#            return self.z
#        return MathFunc( lambda w: Polar(w*self.p, 90) )


def series(*cpts):
    Z = Polar(0.0, 0.0)
    for cpt in cpts:
        if cpt.__class__ is MathFunc or issubclass(cpt.__class__, complex):
            Z += cpt
        else:
            Z += cpt.Z()
    return Z

def parallel(*cpts):
    one = Polar(1.0, 0.0)
    Z = Polar(0.0, 0.0)
    for cpt in cpts:
        if cpt.__class__ is MathFunc or issubclass(cpt.__class__, complex):
            Z += one / cpt
        else:
            Z += one / cpt.Z()
    return one / Z