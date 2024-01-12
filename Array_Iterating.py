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




#-------------------------------
# --------------------------------------------------------------------------------------
# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

var_array_4 = np.array([[[1,2,3,4],[6,7,8,9]],[[10,11,12,13],[22,33,4,55]]]) # still 3D

print("\nreturn the actual values for 3D arrays looping")

for i in var_array_4:
    print(i)
    for k in i:
        print(k)
        for j in k:
            print(j)
            print("----------------")

# -------------------- or this way 
print("\nreturn the actual values for 3D arrays looping")

for i in var_array_4:
    for k in i:
        for j in k:
            print(j)


# -----------------------------------------------------------------------------------
# looping actual value of 2 dimentional array
print("\nlooping actual value of 2 dimentional array")

var_array_5 = np.array([[1,2,3,4],[6,7,8,9]])

for i in var_array_5:
    for k in i:
        print(k)


# -----------------------------------------------------------------------------------
# Iterating Arrays Using nditer()

"""The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
It solves some basic issues which we face in iteration.

Iterating on Each Scalar Element
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult 
to write for arrays with very high dimensionality."""

# Iterate through the following 3-D array using nditer() 
var_array_6 = np.array([[[1,2,3,4],[6,7,8,9]],[[10,11,12,13],[22,33,4,55]]]) # still 3D

print("\nIterate through the following 3-D array using nditer() ")
for i in np.nditer(var_array_6):
    print(i)

#------------------onother
var_array_7 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,16],[4,5,6]]]])

var_array_8 = np.array([[[[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3]]]]], ndmin=5)# you created array with 5 dimentions fully specified

print("\nIterate through the following 5-D array using nditer() ")
for i in np.nditer(var_array_8):
    print(i)


print()
print(var_array_7.ndim)
print(var_array_8.ndim)


# -----------------------------------------------------------------------------------
# Iterating Array With Different Data Types
var_array_9 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,16],[4,5,6]]]], dtype='i8')

for i in np.nditer(var_array_9, flags=['buffered'], op_dtypes=['i8']):
  print(i)


print()
for i in np.nditer(var_array_9, flags=['buffered'], op_dtypes=['S']):
  print(i)


# -----------------------------------------------------------------------------------
# terating With Different Step Size
print()

var_array_10 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,16],[4,5,6]]]])

# with 5 dimentional array 
for i in np.nditer(var_array_10[:,::2]):
  print(i)

#----------------------
# another value skipp with 2 dimentional array
var_array_11 = np.array([[1,2,3,4],[6,7,8,9]])
print()

for i in np.nditer(var_array_11[:,::2]):
    print(i)


# -----------------------------------------------------------------------------------
# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.

# 2D
print()
var_array_12 = np.array([[1,2,3,4],[6,7,8,9]])

for idx, x in np.ndenumerate(var_array_12):
  print(idx, x)


# -----------------------------------
# 3D
print()
var_array_13 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,16],[4,5,6]]]])
for idx, x in np.ndenumerate(var_array_13):
  print(idx, x)


# -----------------------------------
# 5D
print()
var_array_14 = np.array([[[[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3]]]]], ndmin=5)

for idx, x in np.ndenumerate(var_array_14):
  print(idx, x)


# -------------------------------------------------------------------------------------

# -----------------------------------
print()
