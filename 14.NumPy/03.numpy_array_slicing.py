"""
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""

import numpy as np


# Slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])


# Negative Slicing
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])


# Slicing 2-D Arrays
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])


#
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [2, 3, 4, 5, 6]])
print(arr[0:3, 1:4])
