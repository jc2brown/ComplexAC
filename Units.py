
from math import *

units = ['p', 'n', 'u', 'm', '', 'k', 'M', 'G', 'T' ]

unitShift = 4
prec = 3

def getUnit(place):
    chunk = int(place) / 3
    unit = units[chunk + unitShift]
    return unit

def getPlace(n):
    if ( n == 0 ):
        return 1;
    place = floor(log10(abs(n)))
    return place


def getUnits(n):
    if ( abs(n) < 1e-12 ):
        n = 0
    place = getPlace(n)
    unit = getUnit(place)
    shift = (place - place % 3)
    n = n / 10 ** shift
    n = int(n * 10.0**prec) / 10.0**prec
    return (n, unit)

def printUnits(n):
    x = getUnits(n)
    return str(x[0]) + x[1]
    
    
print printUnits(.000000000001)