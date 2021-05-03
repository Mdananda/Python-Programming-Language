print()
#Start Program

import numpy as np
ar = np.array([2, 3], ndmin = 5, dtype="int")
print(ar)
print(ar.dtype)
print(ar.ndim)

ar = np.logspace(1, 40, 5, base=np.e)
print(ar)
print("%.3f" %ar[0])

#--------Mattrix Create--------
ar = np.zeros(3, int)
print(ar)

#--------One values Mattrix--------
ar = np.ones(3, int)
print(ar)

#--------Korno Mattrix---------
ar = np.eye(4, dtype="int")
print(ar)

#--------Full Mattrix----------
ar = np.full((3, 5), 10)
print(ar)

#------Diagonal Mattrix--------
ar = np.diag([2, 3, 4])
print(ar)