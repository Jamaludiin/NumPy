# NumPy Trigonometric Functions
# Trigonometric Functions
    # NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

import numpy as np

# --------------------------------------------------------------------------
# Find sine value of PI/2:

var_sin = np.sin(np.pi/2)

print(var_sin)


var_sin = np.sin(np.pi/4)

print(var_sin)
# --------------------------------------------------------------------------
# Find sine values for all of the values in arr:
var_array = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6, np.pi/7])

var_sin = np.sin(var_array)

print("\nFind sine values for all of the values in arr")
print(var_sin)

# -------------------
# loop the values
print("\nloop the values")
for i in var_sin:
    print(i)

# --------------------------------------------------------------------------
# Convert Degrees Into Radians
    # By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
    # Note: radians values are pi/180 * degree_values.

var_90 = 90
var_180 = 180
var_270 = 270
var_360 = 360

var_array = np.array([np.pi/var_90, np.pi/var_180, np.pi/var_270, np.pi/var_360])

var_sin = np.sin(var_array)

# loop the values
print("\nloop the values of the degrees converted to radius")
var_array = np.array([var_90,var_180,var_270,var_360])
j = 0
for i in var_sin:
    print("The Degrees of",var_array[j],"is converted radius",i)
    j+=1

# --------------------------------------------------------------------------
# short form of the above is 
# loop the values
print("\nloop the values of the degrees converted to radius")
var_array = np.array([90,180,270,360])

j = 0
for i in var_array:
    print("The Degrees of",var_array[j],"is converted radius",np.array([np.pi/var_array[j]]))
    j+=1

# --------------------------------------------------------------------------
