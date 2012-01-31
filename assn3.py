from Components import *
from Complex import *


print "Q1"
E = Polar(12, 0)
L = Ind(None).setReac(6)
C1 = Cap(None).setReac(8)
C2 = Cap(None).setReac(12)

Z = series(L, parallel(C1, C2))
I = E / Z
Vl = I / L.Z()
I2 = I * C2.Z() / (C1.Z() + C2.Z())
I3 = I * C1.Z() / (C1.Z() + C2.Z())
assert I == I2 + I3
print 'I = ' + I.pStr()
print 'Vl = ' + Vl.pStr()
print 'I2 = ' + I2.pStr()
print 'I3 = ' + I3.pStr()



print "\nQ2"
E = Polar(60, 30)
R1 = Res(4.7)
R2 = Res(9.1)
C = Cap(None).setReac(12)

Z = parallel(R1, series(R2, C))
I = E / Z
I1 = I * Z / R1.Z()
I2 = I * Z / series(R2, C)
assert I == (I1 + I2)
print 'I = ' + I.pStr()
print 'I1 = ' + I1.pStr()
print 'I2 = ' + I2.pStr()
print 'I1 + I2 = ' + (I1 + I2).pStr()



print "\nQ3"
E = Polar(40, 0)
R1 = Res(10)
R2 = Res(20)
C = Cap(None).setReac(60)
L = Ind(None).setReac(80)

Z1 = parallel(R2, L)
Z2 = series(R1, Z1)
Z = parallel(C, Z2)
Is = E / Z
I2 = I * Z / Z2
Il = I2 * Z1 / L.Z()
Vl = Il * L.Z()
print 'Is = ' + Is.pStr()
print 'Vl = ' + Vl.pStr()



print "\nQ4"
E = Polar(sqrt(2)*50, 0)
w = 2*pi*1000
R1 = Res(300)
L1 = Ind(0.1)
L2 = Ind(0.2)
C = Cap(1e-6)

Z2 = parallel(C, L2)
Z1 = series(L1, Z2)
Zt = series(R1, Z1)
Is = E / Zt
I1 = Is * Z2 / C.Z()
I2 = Is * Z2 / L2.Z()
assert Is(w) == (I1 + I2)(w)
Vab = Is * Z1
V1 = I2 * L2.Z()
print 'Zt = ' + Zt(w).pStr()
print 'Is = ' + Is(w).iStr()
print 'I1 = ' + I1(w).iStr()
print 'I2 = ' + I2(w).iStr()
print 'Vab = ' + Vab(w).iStr()
print 'V1 = ' + V1(w).iStr()



print '\nQ5'
E = Polar(50, 0)
R1 = Res(2)
R2 = Res(3)
R3 = Res(10)
C1 = Cap(None).setReac(9)
C2 = Cap(None).setReac(2)
L = Ind(None).setReac(6)

Z1 = series(R1, C2)
Z2 = series(R2, C1, L)
Z = parallel(Z1, Z2, R3.Z())
I = E / Z
print 'I = ' + I.pStr()




