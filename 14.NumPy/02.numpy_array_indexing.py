import numpy as np


# access
arr = np.array([1, 2, 3, 4])
print(arr[0])


# Access 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("2nd element on 1st row: ", arr[0, 1])


# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])


# Negative Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd dim: ", arr[1, -1])
