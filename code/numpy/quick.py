from numpy import *

m = mat(random.rand(4,4))
inv = m.I
print m
print inv
print m*inv-eye(4)