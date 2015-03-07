import numpy
import numpy.fft
import matplotlib.pyplot

x=numpy.linspace(0,2*numpy.pi, 20)
wave=numpy.cos(x)
trans=numpy.fft.fft(wave)

print numpy.all(numpy.abs(numpy.fft.ifft(trans)-wave) < 10**-9)

matplotlib.pyplot.plot(trans)


shifted=numpy.fft.fftshift(trans)

matplotlib.pyplot.plot(shifted)
matplotlib.pyplot.show()