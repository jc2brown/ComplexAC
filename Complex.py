from math import *
from MathFunc import *
from UNum import *
from cmath import phase

precision = 4
normalize = False

class Complex(complex):
    
    cmplx = None
    r = None
    o = None  
    
    def __init__(self, *args):
        if ( len(args) == 1 ):
            real = args[0].real
            imag = args[0].imag
        else:
            real = args[0]
            imag = args[1]
        self.cmplx = complex(snap(real), snap(imag))
        self.r = abs(self())
        self.o = r2d(phase(self()))
        

    ''' To-string methods '''     
    def __str__(self):
        return self.cStr() + ' --- ' + self.pStr() + ' --- ' + self.iStr()
        
    def cStr(self):
        return str(UNum(self.real)) + sign(self.imag) + 'j' + str(UNum(abs(self.imag)))
    
    def pStr(self):
        return str(UNum(self.r)) + ' < ' + str(UNum(self.o))
    
    def iStr(self):
        def fOff():
            if ( not normalize ):
                return (' sin', 0)
            if (self.o < -90):
                return (' cos', 90)
            elif (self.o < 0):
                return (' sin', 0)
            elif (self.o < 90):
                return (' sin', 0)
            else:
                return (' cos', -90)
        f, off = fOff();
        return str(UNum(self.r)) + f + ' (wt' + sign(self.o) + str(UNum(abs(self.o + off))) + ')'
    
    
    ''' Operators '''
   
    def __add__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self + c(w) )
        return Complex( complex.__add__(self.cmplx, c.cmplx) )
    
    def __sub__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self - c(w) )
        return Complex( complex.__sub__(self.cmplx, c.cmplx) )
        
    def __mul__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self * c(w) )
        return Complex( complex.__mul__(self.cmplx, c.cmplx) )   
    
    def __div__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self / c(w) )
        return Complex( complex.__div__(self.cmplx, c.cmplx) )
    
    def __eq__(self, c):
        return complex(0.0) == Complex(self - c).cmplx
        
    def __call__(self, *n):
        return self
    
    
            
        
class Polar(Complex):
    def __init__(self, r, o):
        o = d2r(o)
        Complex.__init__(self, r * cos(o), r * sin(o))
        
        
class Cart(Complex):
    def __init__(self, x, y):
        Complex.__init__(self, x, y)
        
 

def sign(n):
    if (n < 0):
        return ' - '
    return ' + '

def r2d(o):
    return o * 180 / pi

def d2r(o):
    return o * pi / 180

