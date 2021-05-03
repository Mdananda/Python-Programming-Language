print()
#Start Program

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 10, 16, 20])
y = np.array([20, 30, 54, 80])
plt.subplot(2, 4, 1)
plt.plot(x, linestyle = "none", marker = 'x', color = 'hotpink')
plt.title("Ananda")
plt.show()

plt.subplot(2, 4, 2)
plt.plot(y, linestyle = "dotted", marker ='X', color = 'tomato')
plt.title("Shuvo")
plt.show()