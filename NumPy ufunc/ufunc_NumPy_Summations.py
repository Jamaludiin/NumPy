# NumPy Summations
import numpy as np

"""
Summations
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements.
"""

# --------------------------------------------------------------------------
# Add the values in arr1 to the values in arr2:
var_array_1 = [1,2,3,4]
var_array_2 = [1,2,3,4]

var_result = np.add(var_array_1,var_array_2)
print("Using the add method in numpy")
print(var_result)

# --------------------------------------------------------------------------
# um the values in arr1 and the values in arr2:
var_result = np.sum([var_array_1,var_array_2]) # 20

print("\nUsing the sum method in numpy")
print(var_result)


# --------------------------------------------------------------------------
# Summation Over an Axis
    # If you specify axis=1, NumPy will sum the numbers in each array.
var_result = np.sum([var_array_1, var_array_2], axis=1)

print("\nUsing the sum method with axis parameter in numpy")
print(var_result)

# --------------------------------------------------------------------------
# Cummulative Sum
    # Cummulative sum means partially adding the elements in array.
    # E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
    # Perfom partial sum with the cumsum() function.

var_result = np.cumsum(var_array_1)
print("\nUsing the cumsum method in numpy")
print(var_result)

var_result = np.cumsum(var_array_2)
print("\nUsing the cumsum method in numpy")
print(var_result)
