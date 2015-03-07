import numpy
import sys
import matplotlib.pyplot

n=int(sys.argv[1])
weights=numpy.ones(n)/n

print weights

c=numpy.loadtxt("E:\\python\\code\\numpy\\data.csv",delimiter=",",usecols=(6,),unpack=True)
sma=numpy.convolve(c,weights)[n-1:-n+1]

t=numpy.arange(n-1,len(c))
matplotlib.pyplot.plot(t,c[n-1:],lw=0.1)
matplotlib.pyplot.plot(t,sma,lw=0.1)
matplotlib.pyplot.show()