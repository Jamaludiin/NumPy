# NumPy LCM Lowest Common Multiply

import numpy as np

# --------------------------------------------------------------------------
# Finding LCM (Lowest Common Multiple)
    # The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

var_num_1 = 5
var_num_2 = 2

var_result = np.lcm(var_num_1, var_num_2)
print("\nFinding LCM in value 5 and 2")
print(var_result)

# --------------------------------------------------------------------------
var_num_1 = 4
var_num_2 = 3

var_result = np.lcm(var_num_1, var_num_2)
print("\nFinding LCM in value 4 and 3")
print(var_result)

# --------------------------------------------------------------------------
var_num_1 = 4
var_num_2 = 6

var_result = np.lcm(var_num_1, var_num_2)
print("\nFinding LCM in value 4 and 6")
print(var_result)

# --------------------------------------------------------------------------
# Finding LCM in Arrays
    # To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
    # The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.

var_num_1 = [2,4,5,4]

var_result = np.lcm.reduce(var_num_1)
print("\nFinding LCM in Arrays")
print(var_result)

# --------------------------------------------------------------------------
# Find the LCM of all values of an array where the array contains all integers from 1 to 10:
var_num_1 = np.arange(1,11)

var_result = np.lcm.reduce(var_num_1)
print("\nFinding LCM in Arrays")
print(var_result)