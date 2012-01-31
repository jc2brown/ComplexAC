
from math import *

units = ['p', 'n', 'u', 'm', '', 'k', 'M', 'G', 'T' ]

unitShift = 4
prec = 3

def getUnit(place):
    chunk = int(place) / 3
    unit = units[chunk + unitShift]
    return unit

def getPlace(n):
    place = floor(log10(n))
    return place


def getUnits(n):
    place = getPlace(n)
    unit = getUnit(place)
    shift = (place - place % 3)
    n = n / 10 ** shift
    n = int(n * 10.0**prec) / 10.0**prec
    return (n, unit)


n = 0.0000045678
x = getUnits(n)

base = x[0]
unit = x[1]

print str(base) + unit