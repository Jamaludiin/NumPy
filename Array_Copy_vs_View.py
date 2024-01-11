# The Difference Between Copy and View
"""The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view."""

import numpy as np


# copy an array to another variable 
var_array_1 = np.array([1, 2, 3, 4, 5])
var_copy = var_array_1.copy()
var_array_1[0] = 42

# Remember, The copy SHOULD NOT be affected by the changes made to the original array.
print(var_array_1) # affected by the changes
print(var_copy) # not affected

print()
# check their data type
print(var_array_1.dtype)
print(var_copy.dtype)


# -------------------------------------------------------------------------------
var_array_2 = np.array([[1,2,3,4],[5,6,7,8]])
var_view = var_array_2.view()
var_array_2[1,3] = 9 # you cannot add new value in one set, u can change the exsiting one for now

# Remember, The original array SHOULD be affected by the changes made to the view.
print(var_array_2) # affected by the changes
print()
print(var_view) # affected also

print()
# check their data type
print(var_array_2.dtype)
print(var_view.dtype)

var_array_2[0:1,3] = 9 # change both row and replace it the index 3

print()
print(var_array_2) # affected by the changes
print()
print(var_view) # also affected

# -------------------------------------------------------------------------------
# Check if Array Owns its Data
"""
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.
"""
print()

print(var_array_1.base) # returns None if the array owns the data.
print(var_copy.base) # returns None if the array owns the data.

print()

print(var_array_2.base) # returns None if the array owns the data.
print(var_view.base) # it does not return none, the base  attribute refers to the original object.

# recap
"""
The copy returns None.
The view returns the original array.
"""