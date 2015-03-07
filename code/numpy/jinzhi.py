import numpy as np

cashflow=np.random.randint(100,size=5)
print cashflow
cashflow=np.insert(cashflow,0,-100)
print cashflow

print np.npv(0.03,cashflow)