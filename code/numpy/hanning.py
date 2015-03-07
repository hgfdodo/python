import numpy
import matplotlib.pyplot
import sys

n=int(5)
weights=numpy.hanning(n)

bhp=numpy.loadtxt("BHP.csv",delimiter=',',usecols=(6,),unpack=True)
bhp_return=numpy.diff(bhp)/bhp[:-1]
bhp_smooth=numpy.convolve(weights/weights.sum(),bhp_return)[n-1:-n+1]

print bhp_return

vale=numpy.loadtxt("VALE.csv",delimiter=',',usecols=(6,),unpack=True)
vale_return=numpy.diff(vale)/vale[:-1]
vale_smooth=numpy.convolve(weights/weights.sum(),vale_return)[n-1:-n+1]

t=numpy.arange(n-1,len(bhp_return))

matplotlib.pyplot.plot(t,bhp_smooth,lw=0.2)
matplotlib.pyplot.plot(t,bhp_return[n-1:],lw=0.1)

matplotlib.pyplot.show()