import numpy
a=numpy.arange(100,1000)
b=numpy.outer(a,a)
numbers=numpy.ravel(b)
numbers.sort()
help(numbers.sort)
j=0
for i in xrange(-1,-1*len(numbers),-1):
	number =str(numbers[i])
	if number == number[::-1]:
		print len(numbers)+i + 1
		print number
		break;