#Statistical Operations
import numpy as np

# Array for examples
arr = np.array([1, 2, 3, 4, 5, 6])
print("Array:", arr)

# 1. Mean
print("Mean:", np.mean(arr))

# 2. Median
print("Median:", np.median(arr))

# 3. Maximum
print("Maximum:", np.max(arr))

# 4. Minimum
print("Minimum:", np.min(arr))

# 5. Sum
print("Sum:", np.sum(arr))

# 6. Standard Deviation
print("Standard Deviation:", np.std(arr))

# 7. Variance
print("Variance:", np.var(arr))

# 8. Percentile
print("50th Percentile (Median):", np.percentile(arr, 50))
print("90th Percentile:", np.percentile(arr, 90))

# 9. Argmax (Index of max value)
print("Argmax (Index of max):", np.argmax(arr))

# 10. Argmin (Index of min value)
print("Argmin (Index of min):", np.argmin(arr))

# 11. 2D Array Statistical Operations
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("2D Array:\n", matrix)

print("Mean (axis=0):", np.mean(matrix, axis=0))  # Column-wise
print("Mean (axis=1):", np.mean(matrix, axis=1))  # Row-wise

