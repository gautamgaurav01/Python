#Arithmetic Operation
import numpy as np

# Arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 1D Arithmetic Operations
print("Addition:", np.add(a, b))
print("Subtraction:", np.subtract(a, b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))


# 2D Arrays
x = np.array([[1, 2, 3], [4, 5, 6]])

y = np.array([[6, 5, 4], [3, 2, 1]])

print("\n2D Addition:\n", np.add(x, y))
print("\n2D Subtraction:\n", np.subtract(x, y))
print("\n2D Multiplication:\n", np.multiply(x, y))
print("\n2D Division:\n", np.divide(x, y))

# Sum operations
print("\nTotal Sum:", np.sum(x))
print("Sum along axis 0 (columns):", np.sum(x, axis=0))
print("Sum along axis 1 (rows):", np.sum(x, axis=1))
