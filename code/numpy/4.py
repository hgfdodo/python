import matplotlib.pyplot
import scipy.misc

lena=scipy.misc.lena()

xmax,ymax = lena.shape[0],lena.shape[1]

lena[range(xmax),range(ymax)]=0
lena[range(xmax-1,-1,-1),range(ymax)]=0

matplotlib.pyplot.imshow(lena)