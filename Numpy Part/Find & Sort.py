print()
#Start Program

import numpy as np
nm = np.array([6, 8, 9, 9, 9])
#nm = np.sort(nm)
print("Order array = ", nm)
X = np.where(nm == 19)
print(X)

x = np.searchsorted(nm, 7) #Searchsorted is working like as binary search.
print(x)