import numpy.random
import numpy.testing
import matplotlib.pyplot
import scipy.misc

lena=scipy.misc.lena()

xmax=lena.shape[0]
ymax=lena.shape[1]

def shuffle_aixs(size):
	a=numpy.arange(size)
	numpy.random.shuffle(a)

	return a

xindexs=shuffle_aixs(xmax)
yindexs=shuffle_aixs(ymax)

numpy.testing.assert_equal(len(xindexs),xmax)
numpy.testing.assert_equal(len(yindexs),ymax)

matplotlib.pyplot.imshow(lena[numpy.ix_(xindexs,yindexs)])
matplotlib.pyplot.show()