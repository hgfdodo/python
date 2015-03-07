import matplotlib.pyplot
import scipy.misc

lena=scipy.misc.lena()

acopy=lena.copy()
aview=lena.view()
bview=lena.view()

matplotlib.pyplot.imshow(acopy)