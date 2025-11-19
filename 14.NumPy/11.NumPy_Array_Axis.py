
#get minimum value with axes in numpy

import numpy as np

n=np.array([[2,3,4,5,6], [15,25,35,45,55], [100,200,300,400,500]])
print("Iterating 2D Array:---")
for a in n:
    print(a)

print("\nMinimun value: " , n.min())
print("\nMinimum value with axis 0 (vertical axis) " , n.min(axis=0))
print("\nMinimum value with axis 1 (horizontal axis) " , n.min(axis=1))
