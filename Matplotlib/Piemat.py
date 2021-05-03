print()
#Start Program

import matplotlib.pyplot as plt
import numpy as np
x = [2, 4, 5]
lb = ['A', "B", "C"]
mm = [.02, .1, 0]
plt.pie(x, labels=lb, explode=mm, startangle= 90, shadow= True)
plt.legend(title = 'ABC')
plt.show()