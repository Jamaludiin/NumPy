# Array Reshaping
"""
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.
"""

import numpy as np

# Reshape From 1-D to 2-D
# this example we Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:

var_array_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16])
var_array_reshaped_1 = var_array_1.reshape(5,3)


print(var_array_1)
print(var_array_reshaped_1)

print()

print(var_array_1.shape)
print(var_array_reshaped_1.shape)

print()
print(var_array_1.ndim)
print(var_array_reshaped_1.ndim)

# ---------------------------------------------------------------------------------------------
# Reshape From 1-D to 3-D
# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
print()

var_array_2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

var_array_reshaped_2 = var_array_2.reshape(2, 3, 2)

print(var_array_2)
print(var_array_reshaped_2)

print()

print(var_array_2.shape)
print(var_array_reshaped_2.shape)

print()
print(var_array_2.ndim)
print(var_array_reshaped_2.ndim)

# ---------------------------------------------------------------------------------------------
# Returns Copy or View?
# Check if the returned array is a copy or a view:
var_array_3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

print()

print(var_array_3.reshape(2, 8).base)
print(var_array_3.reshape(4, 4).base)

# if the example above returns the original array, it means it is a view.


# ---------------------------------------------------------------------------------------------
# Unknown Dimension
"""You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.
"""
var_array_4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# Convert 1D array with 16 elements to 3D array with 2x4 elements:
var_array_reshaped_4 = var_array_4.reshape(2, 4, -1)

print()
print(var_array_reshaped_4)
print(var_array_reshaped_4.ndim)


# ---------------------------------------------------------------------------------------------      
#Flattening the arrays
"""Flattening array means converting a multidimensional array into a 1D array.
We can use reshape(-1) to do this.
"""

# Convert 3D array to 1D by Flattening the arrays
var_array_flatened_5 = var_array_reshaped_4.reshape(-1)

print()
print(var_array_flatened_5)
print(var_array_flatened_5.ndim)