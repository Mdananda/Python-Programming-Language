print()
#Start Program

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 3, 4, 5, 6])
y = np.array([4, 6, 8, 9, 10])
sz = [100, 11, 12, 13, 14]
plt.scatter(x, y, s = sz, c = 'tomato', marker='o', cmap= 'nipy_spectral', alpha= .3)
plt.colorbar()
plt.show()