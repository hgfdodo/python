import numpy
import numpy.linalg
import matplotlib.pyplot

def phi(n):
	a=numpy.mat("1 1;1 0")
	return a**n

print phi(111)[0,0]
#pp=numpy.frompyfunc(phi,1,1)

#print pp(111)[0,0]

c=numpy.mat("0 1 2; 1 0 3; 4 -3 8")
cl=numpy.linalg.inv(c)
print c
print cl
print c*cl