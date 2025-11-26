import numpy as np

# Original 1-D array
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 1-D to 2-D
arr_2d = arr1d.reshape(4, 3)
print("1-D to 2-D:\n", arr_2d)

# 1-D to 3-D
arr_3d = arr1d.reshape(2, 3, 2)
print("\n1-D to 3-D:\n", arr_3d)

# 2-D to 3-D
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_2d_to_3d = arr2d.reshape(2, 2, 2)
print("\n2-D to 3-D:\n", arr_2d_to_3d)

# 2-D to 1-D
arr_2d_to_1d = arr2d.reshape(-1)
print("\n2-D to 1-D:\n", arr_2d_to_1d)

# 3-D to 1-D
arr_3d_to_1d = arr_3d.reshape(-1)
print("\n3-D to 1-D:\n", arr_3d_to_1d)

# 3-D to 2-D
arr_3d_to_2d = arr_3d.reshape(3, 4)
print("\n3-D to 2-D:\n", arr_3d_to_2d)
