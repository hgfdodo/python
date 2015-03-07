import matplotlib.pyplot
import scipy.misc

lena=scipy.misc.lena()

#original picture
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.imshow(lena)

# y turn
yturn=lena[:,::-1]
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.imshow(yturn)

#part
part=lena[:lena.shape[0]/2,:lena.shape[1]/2]
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.imshow(part)

#ood=0
mask=lena%2==0
mask_lena=lena.copy()
mask_lena[mask]=0
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.imshow(mask_lena)