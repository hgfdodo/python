import urllib2
import scipy.io.wavfile
import matplotlib.pyplot
import numpy

response=urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
WAV_FILE="smashingbaby.wav"
filehandle=open(WAV_FILE,'w')
filehandle.write(response.read())
filehandle.flush()
filehandle.close()

rate,data=scipy.io.wavfile.read(WAV_FILE)

matplotlib.pyplot.subplot(211)
matplotlib.pyplot.title("original")
matplotlib.pyplot.plot(data)

newdata=data*0.2
newdata=newdata.astype(numpy.uint8)

scipy.io.wavfile.write("a.wav",rate,newdata)

matplotlib.pyplot.subplot(212)
matplotlib.pyplot.title("new")
matplotlib.pyplot.plot(newdata)
matplotlib.pyplot.show()