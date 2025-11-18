"""
Joining NumPy Arrays
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, along
with the axis. If axis is not explicitly passed, it is taken as 0.
"""

#concatenate() method
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))
print("\nconcatenate()")
print(arr)
 

#stack() method
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2))
print("\nstack()")
print(arr)

#hstack() method
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.hstack((arr1, arr2))
print("\nhstack()")
print(arr)


#vstack() method
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.vstack((arr1, arr2))
print("\nvstack()")
print(arr)

#dstack() method
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.dstack((arr1, arr2))
print("\ndstack()")
print(arr)


#column_stack() method
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.column_stack((arr1, arr2))
print("\ndstack()")
print(arr)