# Finding GCD 
# NumPy GCD Greatest Common Denominator
"""
The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number 
that is a common factor of both of the numbers.
"""

import numpy as np


# Find the HCF of the following two numbers:
var_num_1 = 9
var_num_2 = 6

var_result = np.gcd(var_num_1,var_num_2)

print("Find the HCF of the following two numbers 9 and 6")
print(var_result)

# --------------------------------------------------------------------------
# Finding GCD in Arrays
    # To find the Highest Common Factor of all values in an array, you can use the reduce() method.
    # The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.

var_num_3 = np.array([20,50,90,6,70])

var_result = np.gcd.reduce(var_num_3)

print("\nFinding GCD in Arrays")
print(var_result)

# --------------------------------------------------------------------------
