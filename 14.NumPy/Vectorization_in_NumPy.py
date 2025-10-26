"""Vectorization in NumPy is a method of performing operations on entire arrays without explicit loops."""

#
import numpy as np

a1 = np.array([2, 4, 6, 8, 10])
number = 2
result = a1 + number
print(result)


# Adding two arrays together with vectorization
import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
result = a1 + a2
print(result)


# Element-Wise Multiplication with array
import numpy as np

a1 = np.array([1, 2, 3, 4])
result = a1 * 2
print(result)


# Logical Operations on Arrays
import numpy as np

a1 = np.array([10, 20, 30])
result = a1 > 15
print(result)


# Matrix Operations Using Vectorization
import numpy as np

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
result = np.dot(a1, a2)
print(result)


# Applying Custom Functions with Numpy Vectorize() Function
import numpy as np


def custom_func(x):
    return x**2 + 2 * x + 1


a1 = np.array([1, 2, 3, 4])
result = custom_func(a1)
print(result)


# Vectorization for aggregations operations
import numpy as np

a1 = np.array([1, 2, 3])
result_sum = a1.sum()
result_mean = a1.mean()
print(result_sum)
print(result_mean)
