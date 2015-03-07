import numpy
import matplotlib.pyplot
import numpy.lib.stride_tricks

a=numpy.arange(81)
strides=a.itemsize*numpy.array([27,3,9,1])
shape=(3,3,3,3)
b=numpy.lib.stride_tricks.as_strided(a,shape=shape,strides=strides)

print b