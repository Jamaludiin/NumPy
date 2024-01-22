# NumPy Differences
import numpy as np

# Differences
"""
    A discrete difference means subtracting two successive elements.
    E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
    To find the discrete difference, use the diff() function."""

# Compute discrete difference of the following array:
var_array_1 = [1,2,3,4]

var_result = np.diff(var_array_1)
print("Using the diff method in numpy")
print(var_result)

# --------------------------------------------------------------------------
"""We can perform this operation repeatedly by giving parameter n.
E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , 
then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]"""

# Compute discrete difference of the following array twice:
var_array_2 = [30,20,35,45]

var_result = np.diff(var_array_2, n=2)
print("Using the diff method in numpy")
print(var_result)