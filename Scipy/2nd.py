print()
#Start Program

from scipy.optimize import minimize
from math import cos

def eqe(x):
    return x**2+x*2+5

mymin = minimize(eqe, 3, method='BFGS')
print(mymin)