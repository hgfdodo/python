import numpy
import numpy.linalg

a=numpy.mat("4 11  14;8 7 -2")
b=numpy.linalg.pinv(a)

print a*b

a=numpy.mat("1 2; 1 1")
b=numpy.mat("1 3")

#print a*b
print numpy.dot(b,a)

print numpy.linalg.det(a)