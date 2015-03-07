import numpy
import numpy.linalg

a=numpy.mat("3 -2;1 0")
tz,tx=numpy.linalg.eig(a)
print tz
print tx

print numpy.dot(a,tx[:,1])
print tz[1]*tx[:,1]