import numpy
import matplotlib.pyplot as plt

x=plt.imread("da.jpg")
y=plt.imread("xiao.jpg")

numpy.set_printoptions(threshold='nan')
re= x-y
xx=re.ravel()

plt.plot(xx)
plt.show()