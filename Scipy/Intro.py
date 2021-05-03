print()
#Start Program

from scipy.optimize import root
from math import cos

def eqe(x):
    return x+cos(x)

mycat = root(eqe, 0)
print(mycat.x)