import numpy
import matplotlib.pyplot

points=numpy.zeros(100)
outcomes=numpy.random.hypergeometric(25,1,3,size=len(points))

for i in range(len(points)):
	if outcomes[i]==3:
		points[i]=points[i-1] + 1
	else:
		points[i]=points[i-1] - 6

matplotlib.pyplot.plot(points)
matplotlib.pyplot.show()