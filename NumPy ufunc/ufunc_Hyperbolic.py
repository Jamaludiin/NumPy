# Hyperbolic
import numpy as np

# --------------------------------------------------------------------------
# Hyperbolic Functions
    # NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..

var_Hyperbolic = np.sinh(np.pi/2)

print("Hyperbolic sinh")
print(var_Hyperbolic)
# ---------------
var_Hyperbolic = np.cosh(np.pi/2)

print("\nHyperbolic cosh")
print(var_Hyperbolic)
# ---------------
var_Hyperbolic = np.tanh(np.pi/2)

print("\nHyperbolic tanh")
print(var_Hyperbolic)

# --------------------------------------------------------------------------
# Find cosh values for all of the values in arr:

var_array = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6])

var_Hyperbolic = np.sinh(var_array)

print("\nHyperbolic sinh array")
print(var_Hyperbolic)
# ---------------
var_Hyperbolic = np.cosh(var_array)

print("\nHyperbolic cosh array")
print(var_Hyperbolic)
# ---------------
var_Hyperbolic = np.tanh(var_array)

print("\nHyperbolic tanh array")
print(var_Hyperbolic)


# --------------------------------------------------------------------------
# Finding Angles
    # Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
    # Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

var_Hyperbolic = np.arcsinh(1.0)

print("Hyperbolic Finding Angles arcsinh")
print(var_Hyperbolic)
# ---------------
var_Hyperbolic = np.arccosh(2)

print("\nHyperbolic Finding Angles arccosh")
print(var_Hyperbolic)
# ---------------
var_Hyperbolic = np.arctanh(0.5)

print("\nHyperbolic Finding Angles arctanh")
print(var_Hyperbolic)

# --------------------------------------------------------------------------
# Angles of Each Value in Arrays
var_array = np.array([0.1, 0.2, 0.5])

var_Hyperbolic = np.arctanh(var_array)

print("\nHyperbolic Finding Angles arctanh with array")
print(var_Hyperbolic)