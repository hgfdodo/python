import scipy.misc
import matplotlib.pyplot
import numpy

def get_indices(size):
	arr=numpy.arange(size)
	return arr % 4==0

lena=scipy.misc.lena()
lena1=lena.copy()
lena2=lena.copy()
lena3=lena.copy()

xindices=get_indices(lena.shape[0])
yindices=get_indices(lena.shape[1])
lena1[xindices,yindices]=0
matplotlib.pyplot.subplot(311)
matplotlib.pyplot.imshow(lena1)

lena2[(lena > lena.max()/4) & (lena < lena.max()*3/4)]=0
matplotlib.pyplot.subplot(312)
matplotlib.pyplot.imshow(lena2)

matplotlib.pyplot.subplot(313)
matplotlib.pyplot.imshow(lena3[::-1,:])
matplotlib.pyplot.show()