# Array Iterating in NumPy
# This is for looping purpose
# If we iterate on a 1-D array it will go through each element one by one.

import numpy as np

# --------------------------------------------------------------------------------------
# looping the 1D arrays
var_array_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])

for i in var_array_1:
    print(i)

# --------------------------------------------------------------------------------------
# looping the 1D arrays using the for loop with range and len methods
print("looping the 1D arrays using the for loop with range and len methods")

for i in range(len(var_array_1)):
    print(var_array_1[i])

# --------------------------------------------------------------------------------------
# looping the 1D arrays using the while loop
var_array_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])

print("\nlooping the 1D arrays using the while loop")
i = 0
while i < len(var_array_1):
    print(var_array_1[i])
    i +=1

# -------------------------------- 
# other

print("\nother")
print(var_array_1[0])
print(len(var_array_1))
print(range(len(var_array_1)))


# --------------------------
# --------------------------------------------------------------------------------------
# Iterating 2-D Arrays using for 
print("\nIterating 2-D Arrays using for ")
var_array_2 = np.array([[1,2,3,4],[6,7,8,9]])

for i in var_array_2:
    print(i)

# --------------------------------------------------------------------------------------
# Iterating 2-D Arrays using for with range and len method
print("\nterating 2-D Arrays using for with range and len method")
var_array_2 = np.array([[1,2,3,4],[6,7,8,9]])

for i in range(len(var_array_2)):
    print(var_array_2[i])

# --------------------------------------------------------------------------------------
# Iterating 2-D Arrays using while loop
print("\nIterating 2-D Arrays using while loop")
var_array_2 = np.array([[1,2,3,4],[6,7,8,9]])

i = 0
while i < len(var_array_2):
    print(var_array_2[i])
    i +=1

#-------------------------------
# others
print("\nother")

print(len(var_array_2))
print(range(len(var_array_2)))


#-------------------------------
# --------------------------------------------------------------------------------------
# Iterating 3-D Arrays using for loop
print("\nIterating 3-D Arrays using for loop")

var_array_3 = np.array([[[1,2,3,4],[6,7,8,9],[10,11,12,13]]])

for i in var_array_3:
    print(i)

#-------------------------------
# Iterating 3-D Arrays using for loop
print("\nIterating 3-D Arrays using for loop")

for i in range(len(var_array_3)):
    print("Like this")
    print(var_array_3[i])

#-------------------------------
# Iterating 3-D Arrays using while loop
print("\nIterating 3-D Arrays using while loop")

var_array_3 = np.array([[[1,2,3,4],[6,7,8,9]],[[10,11,12,13],[22,33,4,55]]]) # still 3D

i = 0
while i < len(var_array_3):
    print(var_array_3[i])
    print("Like this")
    i +=1

#-------------------------------
print("\nother")
print(len(var_array_3))
print(range(len(var_array_3)))
print(var_array_3.ndim)

