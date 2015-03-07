import numpy
N=600851475143
LIM=10**6
def factor(n):
	a=numpy.ceil(numpy.sqrt(n))
	lim=min(LIM,n)
	a=numpy.arange(a,a+lim)
	b2=a**2-n

	xiao=numpy.modf(numpy.sqrt(b2))[0]

	indices=numpy.where(xiao==0)

	a=numpy.ravel(numpy.take(a, indices))

	a=int(a)

	b=numpy.sqrt(a**2-n)
	b=int(b)

	c=a+b
	d=a-b

	if c==1 or d==1:
		return
	print c,d
	factor(c)
	factor(d)
factor(N)