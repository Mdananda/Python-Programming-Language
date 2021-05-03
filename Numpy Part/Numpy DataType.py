print()
#Start Program

import numpy as np
nm = np.array([1.3, 2, 3], dtype="i")
print(nm)
nm = nm.astype("bool")
print(nm)
print(nm.dtype)



nn = np.arange(1, 10)
nm = nn.copy()
nm[0] = 100
print(nm.base)