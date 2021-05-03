print()
#Start Program

from numpy import random as rd

np = rd.randint(100, size=(2, 4))
print(np)

print()
np = rd.choice([1, 3, 4, 5], p=[.2, 0.3, 0.5, 0], size=(2, 3))
print(np)

print()
nm = rd.random((4, 5))
print(nm)

print()
nm = rd.rand(2, 2, 3)
print(nm)