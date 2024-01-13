"""
Splitting NumPy Arrays
    Splitting is reverse operation of Joining.

    Joining merges multiple arrays into one and Splitting breaks one array into multiple.

    We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
w3schools.com
"""
import numpy as np
# --------------------------------------------------------------------------------
# 1D array splitting using array_split() method

var_array_1 = np.array([1,2,3,4, 5,6,7,8])
var_array_2 = np.array([[1,2,3,4],[5,6,7,8]])
var_array_3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
var_array_4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

var_array_split_1 = np.array_split(var_array_1,4)
print(var_array_split_1) # Note: The return value is a list containing four arrays.
print(var_array_1.ndim)

print("\nIf the array has less elements than required, it will adjust from the end accordingly.")
var_array_split_1 = np.array_split(var_array_1,5)
print(var_array_split_1) # Note: The return value is a list containing four arrays.

# ---------------------------------
# 2D array splitting using array_split() method
print()
var_array_split_2 = np.array_split(var_array_2,3)
print(var_array_split_2)
print(var_array_2.ndim)

# ---------------------------------
"""
Note: We also have the method split() available but it will not adjust the elements when elements are 
less in source array for splitting like in example above, array_split() worked properly but split() would fail.
"""
print()
var_array_1 = np.array([1,2,3,4, 5,6,7,8])

var_array_split_3 = np.array_split(var_array_1,4)
print(var_array_split_3)

print(var_array_split_3[0])
print(var_array_split_3[1])
print(var_array_split_3[2])


# ---------------------------------
var_array_2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print()

var_array_split_4 = np.array_split(var_array_2,6)
print(var_array_split_4)

print(var_array_split_4[0])
print(var_array_split_4[1])
print(var_array_split_4[2])

# ------------------------------
print()

var_array_split_4 = np.array_split(var_array_2,8)
print(var_array_split_4)

print(var_array_split_4[0])
print(var_array_split_4[1])
print(var_array_split_4[2])

# ------------------------------
print("\nLooping the array splitted")
for i in var_array_split_4:
    print(i)

# ------------------------------
var_array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

print()
var_array_split_4 = np.array_split(var_array_2,3)
print(var_array_split_4)

# ------------------------------
print("\nLooping the array splitted")
for i in var_array_split_4:
    print(i)


# ------------------------------
# Split the 2-D array into three 3-D arrays along rows.
var_array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

print()
var_array_split_4 = np.array_split(var_array_2,3, axis= 1)
print(var_array_split_4)

# ------------------------------
print("\nLooping the array splitted")
for i in var_array_split_4:
    print(i)

# ------------------------------------------------------------------------------------------------
# An alternate solution is using hsplit() opposite of hstack()

var_array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

print("\nhsplit")
var_array_split_4 = np.hsplit(var_array_2,3)
print(var_array_split_4)

print("\nhstack")
var_array_split_5 = np.hstack(var_array_2) # hstack() takes 1 positional argumen
print(var_array_split_5)

print("\nNormal values")
print(var_array_2)


# ------------------------------------------------------------------------------------------------
# Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
var_array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

print("\nvsplit")
var_array_split_4 = np.vsplit(var_array_2,3)
print(var_array_split_4)

# ------------------------------
print("\ndsplit")
var_array_2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])

var_array_split_5 = np.dsplit(var_array_2,3) # it works more than 3d arrays
print(var_array_split_5)

print("\nNormal values")
print(var_array_2)