import numpy
import numpy.linalg

a=numpy.mat("4 11 14;8 7 -2")
u,sim,v=numpy.linalg.svd(a,full_matrices=False)
print u,"\n",sim,"\n",v
print u*numpy.diag(sim)*v