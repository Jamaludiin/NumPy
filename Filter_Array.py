# Filter Array

import numpy as np

# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.

var_array = np.array([1, 2, 3, 4, 5, 3, 6]) # it has to match the nuber of lines in var_array_bool

var_array_bool = [True, False, True, False,False, True, False]

var_result = var_array[var_array_bool]

"""var_result = var_array[True] # it will print all the values
var_result = var_array[False] # it will print empy tuple"""

print(var_result)

# ---------------------------
# Create a filter array that will return only values higher than 42:
var_array_1 = np.array([1, 2, 3, 4, 5, 3, 3, 6, 2, 4, 7, 6])

var_greater_two = []

for i in var_array_1:
    if i > 2:
        var_greater_two.append(True)
    else:
     var_greater_two.append(False)

print("\ngreater than two values")
print(var_greater_two)

print("\nfilter them now")
var_filter_1 = var_array_1[var_greater_two]
print(var_filter_1)

# ---------------------------
# Create a filter array that will return only even elements from the original array:

var_array_1 = np.array([1, 2, 3, 4, 5, 3, 3, 6, 2, 4, 7, 6])

var_greater_two = []

for i in var_array_1:
    if i % 2 == 0:
        var_greater_two.append(True)
    else:
     var_greater_two.append(False)

print("\nDivisble by 2")
print(var_greater_two)

print("\nfilter them now")
var_filter_1 = var_array_1[var_greater_two]
print(var_filter_1)


# ---------------------------
# Creating Filter Directly From Array
    # The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
    # We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

var_array_2 = np.array([1,2,3,44,5,6,77,8,99,8,777])

var_bool_2 = var_array_2 > 2

var_filter_2 = var_array_2[var_bool_2]

print("\nEasy filteration")
print(var_filter_2)
print(var_bool_2)

# ------------------------------
# Create a filter array that will return only even elements from the original array:
var_array_2 = np.array([1,2,3,44,5,6,77,8,99,8,777])

var_bool_2 = var_array_2 % 2 == 0

var_filter_2 = var_array_2[var_bool_2]

print("\nEven numbers in the array by doing filteration")
print(var_filter_2)
print(var_bool_2)

# ------------------------------
