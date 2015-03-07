import numpy
import matplotlib.pyplot

cash=numpy.zeros(10000)
cash[0]=1000
outcome=numpy.random.binomial(9,0.5,size=len(cash))

for i in range(1,len(cash)):
	if outcome[i] >= 5:
		cash[i] =cash[i-1] + 1
	else:
		cash[i] =cash[i-1] - 1
print outcome.max(), outcome.min()

matplotlib.pyplot.plot(numpy.arange(10000),cash)
matplotlib.pyplot.show()