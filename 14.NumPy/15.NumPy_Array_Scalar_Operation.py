#Scalar_Operation
import numpy as np

# Array
arr = np.array([1, 2, 3, 4])

print("Original Array:", arr)

# 1. Addition
print("Addition (arr + 5):", arr + 5)

# 2. Subtraction
print("Subtraction (arr - 2):", arr - 2)

# 3. Multiplication
print("Multiplication (arr * 3):", arr * 3)

# 4. Division
print("Division (arr / 2):", arr / 2)

# 5. Floor Division
print("Floor Division (arr // 2):", arr // 2)

# 6. Modulus
print("Modulus (arr % 2):", arr % 2)

# 7. Power
print("Power (arr ** 2):", arr ** 2)

# 8. Square Root
print("Square Root:", np.sqrt(arr))

# 9. Exponential
print("Exponential:", np.exp(arr))

# 10. Logarithm
print("Logarithm:", np.log(arr))

# 11. Absolute Value
neg_arr = np.array([-1, -2, 3])
print("Absolute Value:", np.abs(neg_arr))

# 12. Rounding
float_arr = np.array([1.2, 2.5, 3.8])
print("Rounded:", np.round(float_arr))
