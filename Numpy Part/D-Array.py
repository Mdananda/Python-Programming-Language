print()
#Start Program

import numpy as np
#----0 Daimention------
ar0 = np.array(12)
print(ar0)
print("Daimention of Array :", ar0.ndim)

print()
#----1 Daimention--------
ar1 = np.array([1, 2, 3, 4, 5])
print("Daimention of Array :", ar1)
print(ar1.ndim)

print()
#----2 Daimention--------
ar2 = np.array([[1, 2],[3, 4]])
print(ar2)
print("Daimention of Array :",ar2.ndim)

print()
#----2 Daimention--------
ar3 = np.array([[[1, 5],[3, 4]], [[1, 2], [2, 4]]])
print(ar3)
print("Daimention of Array :",ar3.ndim)

print()
#----2 Daimention--------
arx = np.array([1, 2, 3, 4], ndmin = 5)
print(arx)
print("Daimention of Array :",arx.ndim)

print()
#----2 Daimention--------
ar = [[1, 4], [2, 3]]
arx = np.array(ar)
print(arx)
print("Dimension of Array :",arx.ndim)