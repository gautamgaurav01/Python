#
import numpy as np

n = np.array((1, 2, 3))
print(n)

list = np.array([1, 2, 3])
print(list)
print(type(list))

# dimension

# zero d
dime = np.array("gaurav")
print("Dimension: ", dime.ndim)


#1 D
one_d =np.array([1,2,3,4,5])
print ("Dimension: ", one_d.ndim)


#2 D
two_d = np.array([[1,2,3,4] , [5,6,7,8]])
print("Dimension: " , two_d.ndim)


#datatypes

var=np.array(['gaurav','sandesh','puskar'])
print(var.dtype)


var=np.array(['gaurav','sandesh','puskar'], dtype='S5')
print(var.dtype)