# Array Shape
# The shape of an array is the number of elements in each dimension.

# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

import numpy as np

var_array_1 = np.array([1,2,3,4, 5,6,7,8])
var_array_2 = np.array([[1,2,3,4],[5,6,7,8]])
var_array_3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
var_array_4 =np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(var_array_1.shape)
print(var_array_2.shape)
print(var_array_3.shape)
print(var_array_4.shape)

print(np.array([1, 2, 3, 4], ndmin=5).shape)