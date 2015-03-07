import numpy
import numpy.random
import matplotlib.pyplot
n=10000
no=numpy.random.normal(size=n)
dummy,bins,dummy2=matplotlib.pyplot.hist(no,numpy.sqrt(n),normed=True,lw=1)

sigma=1
mu=0
matplotlib.pyplot.plot(bins,1/sigma * numpy.sqrt(numpy.pi*2) * numpy.exp(- (bins-mu)**2 /(2*sigma**2)),lw=2)
matplotlib.pyplot.show()