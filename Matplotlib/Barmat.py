print()
#Start Program

import matplotlib.pyplot as plt
import numpy as np
x = ["A", "B", "C"]
y = [10, 8, 15]
#plt.bar(x, y, width=.5, color = 'tomato')
#plt.show()

nm = np.random.normal(170, 10, 250)
plt.hist(nm)
plt.show()

