print()
#Start Program

import numpy as np
rnd = np.random.rand(2, 3)
print(rnd)

print("\nRand Standard Int")
rnd = np.random.randn(3, 3)
print(rnd)

print("\nRand Int")
rnd = np.random.randint(0, 10, 10, dtype="int64")
print(rnd.reshape(2, 5))

print()
arr = np.arange(1, 10, .5)
print(arr)