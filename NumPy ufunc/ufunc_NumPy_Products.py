# NumPy Products
import numpy as np

"""
Products
To find the product of the elements in an array, use the prod() function.
"""

# --------------------------------------------------------------------------
# Find the product of the elements of this array:
var_array_1 = [1,2,3,4]
var_array_2 = [1,2,3,4]

var_result = np.prod(var_array_1)
print("Using the prod method in numpy")
print(var_result)

# --------------------------------------------------------------------------
# prod same the above
var_result = np.prod([var_array_2]) # 24

print("\nUsing the prod method in numpy")
print(var_result)

# --------------------------------------------------------------------------
# Products Over an Axis
    # If you specify axis=1, NumPy will return the product of each array.
var_result = np.prod([var_array_1, var_array_2], axis=1)

print("\nUsing the prod method with axis parameter in numpy")
print(var_result)

# --------------------------------------------------------------------------
# Cummulative Product
    # Cummulative product means taking the product partially.
    # E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
    # Perfom partial sum with the cumprod() function.

var_result = np.cumprod(var_array_1)
print("\nUsing the cumprod method in numpy")
print(var_result)

var_result = np.cumprod(var_array_2)
print("\nUsing the cumprod method in numpy")
print(var_result)
