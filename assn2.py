from Components import *
from Complex import *


print "Q1"
w = 377
e1 = Polar(3, 30)
e2 = Polar(5, -45 - 90)
e = e1 + e2
print "e = " + str(e(None))


print "\nQ2"
w = 1e4
c = Cap(1e-6)
l = Ind(5.1e-3)
E = Polar(6, -60)
Z = series(c, l)
I = E / Z
print 'E = ' + str(E)
print 'Zc = ' + str(c.Z()(w))
print 'Zl = ' + str(l.Z()(w))
print 'Z = ' + str(Z(w))
print "i = " + str(I(w))
print "vc = " + str(c.V(I)(w))
print "vl = " + str(l.V(I)(w))


print "\nQ3"
w = 1e6
r = Res(1.1e3)
l = Ind(6.45e-6)
E = Polar(10, -30)
Z = series(r, l)
I = E / Z
print 'E = ' + str(E)
print 'Zr = ' + str(r.Z())
print 'Zl = ' + str(l.Z()(w))
print 'Z = ' + str(Z(w))
print "i = " + str(I(w))
print "vr = " + str(r.V(I)(w))
print "vl = " + str(l.V(I)(w))


print "\nQ4"
w = 754
r1 = Res(3e3)
r2 = Res(3e3)
l = Ind(10e-3)
c = Cap(100e-6)
E = Polar(5, -45)
Z = series(parallel(r1, r2), l, c)
I = E / Z
print 'E = ' + str(E)
print 'Zr = ' + str(r.Z())
print 'Zl = ' + str(l.Z()(w))
print 'Zc = ' + str(c.Z()(w))
print 'Z = ' + str(Z(w))
print "i = " + str(I(w))
print "vr = " + str(r.V(I)(w))
print "vl = " + l.V(I)(w).pStr()
print "vc = " + str(c.V(I)(w))

