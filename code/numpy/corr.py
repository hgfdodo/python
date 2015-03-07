import numpy
import matplotlib.pyplot

cbhp=numpy.loadtxt("BHP.csv",delimiter=",",usecols=(6,),unpack=True)
cvale=numpy.loadtxt("VALE.csv",delimiter=",",usecols=(6,),unpack=True)

bhp=numpy.diff(cbhp)/cbhp[:-1]
vale=numpy.diff(cvale)/cvale[:-1]

xie=numpy.cov(bhp,vale)

print xie
print xie.trace()

print "corrcoef:",xie/(numpy.std(bhp) * numpy.std(vale))

print numpy.corrcoef(bhp,vale)