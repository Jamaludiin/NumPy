# NumPy Trigonometric Functions
# Trigonometric Functions
    # NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

import numpy as np

# --------------------------------------------------------------------------
# Find sine value of PI/2:

var_sin = np.sin(np.pi/2)

print(var_sin)

# -------- aother example
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
# find the son values
var_90 = 90
var_180 = 180
var_270 = 270
var_360 = 360

var_array = np.array([np.pi/var_90, np.pi/var_180, np.pi/var_270, np.pi/var_360])

var_sin = np.sin(var_array)
print("\nloop the values of the sin-----------")
print(var_sin)

# loop the values-----------------------
print("\nloop the values of the sin-------------")
var_array_1 = np.array([var_90,var_180,var_270,var_360])

j = 0
for i in var_sin:
    print("The Degrees of",var_array_1[j],"its sin values is",i)
    j+=1

# --------------------------------------------------------------------------
# short form of the above is 
# loop the values
print("\nloop the values of the degrees converted to sin values=========")
var_array = np.array([90,180,270,360])

j = 0
for i in var_array:
    print("The Degrees of",var_array[j],"is converted radius",np.sin(np.array([np.pi/var_array[j]])))
    j+=1

# --------------------------------------------------------------------------
# Convert Degrees Into Radians
    # By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
    # Note: radians values are pi/180 * degree_values.

var_array = np.array([90,180,270,360])

var_degre_radies = np.deg2rad(var_array)
print("\nthe values of the degrees converted to Radians")
print(var_degre_radies)

# --------------------------------------------------------------------------
# short form of the above is 
# loop the values
print("\nloop the values of the degrees converted to Radians")
var_array = np.array([90,180,270,360])

# this converts one by one, tip use multidimentional array for this practice
j = 0
for i in var_array:
    print("The Degrees of",var_array[j],"is converted to Radians",np.deg2rad(np.array([np.pi/var_array[j]])))
    j+=1


# --------------------------------------------------------------------------
# short form of the above but multidimentional array 
# loop the values
print("\nloop the values of the degrees converted to Radians")
var_array = np.array([[[90, 135, 160], [170, 175, 190]], [[210, 240, 260], [280, 300, 360]]])


# tip use multidimentional array for this practice
j = 0
for i in var_array:
    print("The Degrees of",var_array[j],"is converted to Radians",np.deg2rad(np.array([np.pi/var_array[j]])))
    j+=1


# --------------------------------------------------------------------------
# Radians to Degrees

var_array = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]) # these are ways if u want as constatnt or as array

var_radies_degre = np.rad2deg(var_array)
print("\nloop the values of the radias converted to degree")
print(var_radies_degre)

#-----------------------
# tip use array and access each value one by for this practice
var_array = np.array([0.00060923,0.00030462,0.00020308,0.00015231])

print()
j = 0

for i in var_array:
    print("The Degrees of",var_array[j],"is converted to Radians",np.round(np.deg2rad(np.array([np.pi/var_array[j]]))))
    j+=1

# --------------------------------------------------------------------------

# Finding Angles
    # Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
    # NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.

var_angle = np.arcsin(1.0)
print("\nFinding Angles")
print(var_angle)
#-----------------------
var_angle = np.arccos(1.0)
print("\nFinding Angles")
print(var_angle)
#-----------------------
var_angle = np.arctan(1.0)
print("\nFinding Angles")
print(var_angle)

#-----------------------
# Angles of Each Value in Arrays
var_angels = np.array([1, -1, 0.1])
var_angle = np.arcsin(var_angels)
print("\nFinding Angles")
print(var_angle)

# --------------------------------------------------------------------------
# Hypotenues
    # Finding hypotenues using pythagoras theorem in NumPy.
    # NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

var_base = 6
var_perpendicular = 4

var_Hypotenues = np.hypot(var_base,var_perpendicular)

print("\nHypotenues")
print(var_Hypotenues)
#----------------------- still same but the base values enterchanged to perpendicular values
var_base = 4
var_perpendicular = 6

var_Hypotenues = np.hypot(var_base,var_perpendicular)

print("\nHypotenues")
print(var_Hypotenues)