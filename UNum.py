
from math import *

# Unit prefixes
units = ['p', 'n', 'u', 'm', '', 'K', 'M', 'G', 'T' ]
 
# Index of ones unit prefix in units array 
unitShift = 4   

# Numerical precision when printing
precision = 3     

zeroThreshold = 1e-12


class UNum(float):
        
    def __init__(self, n):
        self = n

    def getUnits(self):
        def getUnit(place):
            chunk = int(place) / 3
            unit = units[chunk + unitShift]
            return unit
        def getPlace(n):
            if ( n == 0 ):
                return 1;
            place = floor(log10(abs(n)))
            return place
        
        place = getPlace(self)
        unit = getUnit(place)
        shift = (place - place % 3)
        value = self / 10 ** shift
        value = int(value * 10.0**precision) / 10.0**precision
        return (value, unit)

    def __str__(self):
        x = self.getUnits()
        value = x[0]
        unit = x[1]
        return str(value) + unit
    
    

def snap(n):
    if ( abs(n) < zeroThreshold ):
        return 0.0
    return n

