import numpy
from matplotlib.finance import quotes_historical_yahoo
from datetime import date

today=date.today()
start=(today.year-1,today.month,today.day)

quotes=quotes_historical_yahoo("AAPL",start,today)
close=[q[4] for q in quotes]

states=numpy.sign(numpy.diff(close))

NDIM=3
SM=numpy.zeros((NDIM,NDIM))

signs=[-1,0,1]
k=0.01

for i in xrange(len(signs)):
    start_indices=numpy.where(states[:-1]==signs[i])[0]
    N =len(start_indices) + k*NDIM

    if N==0:
        continue

    end_value=states[start_indices+1]

    for j in xrange(len(signs)):
        occurrences=len(end_value[end_value==signs[j]])
        SM[i][j]=(occurrences + k)/float(N)
print SM
eig_out=numpy.linalg.eig(SM)
print eig_out

idx_dec=numpy.where(numpy.abs(eig_out[0]-1) <0.1)
print "Index eigenvalue 1", idx_dec

x=eig_out[1][:,idx_dec].flatten()
help(eig_out[1][:,idx_dec].flatten)
print "Steedy state vector",x
print "Check",numpy.dot(SM,x)