from math import *
from MathFunc import *
from Units import *

precision = 4

class Complex(object):
    
    x = 0
    y = 0
    r = 0
    o = 0
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
        self.o = 0
        
    def setPolar(self, r, o):
        self.r = r
        self.o = ((o+180) % 360) - 180;
        self.x = r * cos(d2r(o))
        self.y = r * sin(d2r(o))
        
    def setCart(self, x, y):
        self.x = x
        self.y = y
        self.r = sqrt(x**2 + y**2)
        self.o = r2d(atan2(y, x))      
        
    def __str__(self):
        def sign(n):
            if (n < 0):
                return '- '
            return '+ '
        def fOff():
            return (' sin', 0)
#            if (self.o < -90):
#                return (' cos', 90)
#            elif (self.o < 0):
#                return (' sin', 0)
#            elif (self.o < 90):
#                return (' sin', 0)
#            else:
#                return (' cos', -90)
        f, off = fOff();
        return str(rnd(self.x)) + ' + j' + str(rnd(self.y)) + ' --- ' + str(rnd(self.r)) + f + ' (wt ' + sign(self.o) + str(abs(rnd(self.o + off))) + ')'
        
        
    def __add__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self + c(w) )
        return cart(self.x + c.x, self.y + c.y)  
    
    def __sub__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self - c(w) )
        return cart(self.x - c.x, self.y - c.y)   
        
    def __mul__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self * c(w) )
        return polar(self.r * c.r, self.o + c.o)
    
    def __div__(self, c):
        if c.__class__ is MathFunc:
            return MathFunc( lambda w: self / c(w) )
        return polar(self.r / c.r, self.o - c.o)
        
  
def rnd(n):  
    return int(n*10**precision)/10.0**precision
  
def r2d(o):
    return o * 180 / pi

def d2r(o):
    return o * pi / 180

def polar(r, o):
    c = Complex()
    c.setPolar(r, o)
    return c

def cart(x, y):
    c = Complex()
    c.setCart(x, y)
    return c