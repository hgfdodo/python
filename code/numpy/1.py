import scipy
import scipy.misc
import matplotlib.pyplot
import numpy.testing



lena=scipy.misc.lena()
LENA_X=512
LENA_Y=512
numpy.testing.assert_equal((LENA_X,LENA_Y),lena.shape)

yfactor=2
xfactor=3

resized=lena.repeat(yfactor,axis=0).repeat(xfactor,axis=1)
numpy.testing.assert_equal((LENA_X*xfactor,LENA_Y*yfactor),resized.shape)

matplotlib.pyplot.subplot(211)
matplotlib.pyplot.imshow(lena)

matplotlib.pyplot.subplot(212)
matplotlib.pyplot.imshow(resized)

matplotlib.pyplot.show()