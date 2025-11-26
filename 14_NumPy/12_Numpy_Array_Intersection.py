#intersection of array in numpy

import numpy as np
n1= np.array([5,6,7,8,9])
n2= np.array([1,2,3,4,5])

resarr= np.intersect1d(n1,n2)
print("Intersection: " ,resarr)