# Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array.

import numpy as np

# in NumPy we join arrays by axes.

var_array_1 = np.array([1,2,3,4])
var_array_2 = np.array([5,6,7,8])

# to join use concatenate((var1,var2))
var_array_join_1_2 = np.concatenate((var_array_1,var_array_2))

print(var_array_join_1_2)

# ------------------------------
# conactenating 2D
var_array_3 = np.array([[1,2,3,4],[5,6,7,8]])
var_array_4 = np.array([[9,10,11,12],[13,14,15,16]])

var_array_join_3_4 = np.concatenate((var_array_3,var_array_4))

print("\nconactenating 2D")
print(var_array_join_3_4)

# ------------------------------
# Join two 3-D arrays along rows (axis=1):
# conactenating 3D

var_array_5 = np.array([[[1,2,3,4],[5,6,7,8]]])
var_array_6 = np.array([[[9,10,11,12],[13,14,15,16]]])

# axes 1
var_array_join_5_6a = np.concatenate((var_array_5,var_array_6), axis=1)
# axes 2
var_array_join_5_6b = np.concatenate((var_array_5,var_array_6), axis=2)


print("\nJoin two 3-D arrays along rows (axis=1):")
print(var_array_join_5_6a)
print("\nJoin two 3-D arrays along rows (axis=2):")
print(var_array_join_5_6b)
print(var_array_5.ndim)


# ------------------------------------------------------------------------------------
# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
var_array_7 = np.array([1,2,3,4])
var_array_8 = np.array([5,6,7,8])

var_array_stack_1 = np.stack((var_array_7,var_array_8))

print("\nJoining Arrays Using Stack Functions")
print(var_array_stack_1)

# ------------------------------
# stack 3D
var_array_9 = np.array([[[1,2,3,4],[5,6,7,8]]])
var_array_10 = np.array([[[9,10,11,12],[13,14,15,16]]])

var_array_stack_2a = np.stack((var_array_9,var_array_10), axis=1)

var_array_stack_2b = np.stack((var_array_9,var_array_10), axis=2)


print("\nstack 3D axis 1")
print(var_array_stack_2a)

print("\nstack 3D")
var_array_stack_2a = np.stack((var_array_9,var_array_10)) # if not specifed axis it will add two new line space in between
print(var_array_stack_2a)

print("\nstack 3D axes 2")
print(var_array_stack_2b)


# ------------------------------------------------------------------------------------
# ------------------------------
# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.

var_array_11 = np.array([1,2,3,4])
var_array_12 = np.array([5,6,7,8])

var_array_hstack_1 = np.hstack((var_array_11, var_array_12))

print("\nStacking Along Rows")
print(var_array_hstack_1)

# ------------------------------
# hstack 3D
var_array_13 = np.array([[[1,2,3,4],[5,6,7,8]]])
var_array_14 = np.array([[[9,10,11,12],[13,14,15,16]]])

var_array_hstack_2a = np.hstack((var_array_13,var_array_14))

print("\nhstack 3D")
print(var_array_hstack_2a)

# ------------------------------------------------------------------------------------
# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
var_array_15 = np.array([[[1,2,3,4],[5,6,7,8]]])
var_array_16 = np.array([[[9,10,11,12],[13,14,15,16]]])

var_array_vstack_2a = np.vstack((var_array_15,var_array_16))

print("\nvstack 3D")
print(var_array_vstack_2a)


# ------------------------------------------------------------------------------------
# Stacking Along Height (depth)
# 1D
var_array_17 = np.array([1,2,3,4])
var_array_18 = np.array([5,6,7,8])

var_array_dstack_1 = np.dstack((var_array_17, var_array_18))

print("\nStacking Along Height (depth)")
print(var_array_dstack_1)

# ------------------------------
# dstack 3D
var_array_19 = np.array([[[1,2,3,4],[5,6,7,8]]])
var_array_20 = np.array([[[9,10,11,12],[13,14,15,16]]])

var_array_dstack_2 = np.dstack((var_array_19,var_array_20))

print("\ndstack 3D")
print(var_array_dstack_2)