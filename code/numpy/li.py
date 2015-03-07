import numpy
import numpy.linalg

s='1 2 3; 2 0 6; 1 4 8'
a=numpy.mat(s)
b=numpy.array([1,2,3])
val=numpy.linalg.solve(a,b)

print a
print b
print val

print numpy.dot(a,val)