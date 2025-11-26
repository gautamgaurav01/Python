"""
Shape of an Array
The shape of an array is the number of elements in each dimension.
"""

# 0-D
import numpy as np

array = np.array(66)
print(array)
print(array.shape)  # shape of array

# 1-D
array_1d = np.array([1, 2, 3, 4])
print(array_1d)
print(array_1d.shape)  # shape of array


# 2-D
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(array_2d)
print(array_2d.shape)  # shape of array


# 3D
array_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 8, 7, 6], [4, 3, 2, 1]]])
print(array_3d)
print(array_3d.shape)  # shape of array
