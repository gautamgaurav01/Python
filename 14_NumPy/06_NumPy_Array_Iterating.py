"""
Iterating Arrays
Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.
"""

# 1-D
import numpy as np

arr = np.array([1, 2, 3])
print("1-D Iterating")
for x in arr:
    print(x)


# 2-D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Iterating")
for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)


# 3-D

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D Iterating")
for x in arr:
    print(x)
for x in arr:
    for y in x:
        for z in y:
            print(z)
