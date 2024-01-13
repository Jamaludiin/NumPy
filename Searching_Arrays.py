"""
Searching Arrays
    You can search an array for a certain value, and return the indexes that get a match.

    To search an array, use the where() method.
"""
import numpy as np

# Using where() method
var_array_1 = np.array([1,2,3,4,5,6,7])

# You can search an array for a certain value, and return the indexes that get a match.
var_search_1 = np.where(var_array_1==4) # it returns index 3 which 4 is found as tuple

print(var_search_1)

# ---------------------------
var_array_2 = np.array([1,2,3,4,5,6,7,3,4,5,4])
var_search_2 = np.where(var_array_2==4) # it returns index 3,8,10 which 4 is found multiple time as tuple

print()
print(var_search_2)


# -------------------------
# Find the indexes where the values are even:
var_array_2 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_3 = np.where(var_array_2%2 == 0)

print("\nSearching even values in the array")
print(var_search_3)

# ---------------------------
# Find the indexes where the values are odd number:
var_array_2 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_3 = np.where(var_array_2%2 == 1)

print("\nSearching odd values in the array")
print(var_search_3)

# ---------------------------
# search multidimentional array
var_array_2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])
var_search_4 = np.where(var_array_2 == 17)

print("\nSearching from 3D array")
print(var_search_4)

# ---------------------------------------------------------------------------------------------------
"""
Search Sorted
    There is a method called searchsorted() which performs a binary search in the array, and returns 
    the index where the specified value would be inserted to maintain the search order.

    The searchsorted() method is assumed to be used on sorted arrays.
"""

var_array_3 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_5 = np.searchsorted(var_array_3, 5)

print("\nSearching in the array")
print(var_search_5)

# -------------------------
# Search From the Right Side
# By default the left most index is returned, but we can give side='right' to return the right most index instead.

var_array_4 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_6 = np.searchsorted(var_array_4, 5, side='right') # i think he skip the duplicate value such as 4 only counts once

print("\nSearch From the Right Side")
print(var_search_6)

# -------------------------
var_array_5 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_7 = np.searchsorted(var_array_5, 7, side='left') # it returns 11, becos the data was sorted the searcherd then its position is 11 not its index

print("\nSearch From the Left Side")
print(var_search_7)
print("\nSorted array data")
print(np.sort(var_array_5))


# ---------------------------------------------------------------------------------------------------
# Searching Multiple Values
# To search for more than one value, use an array with the specified values.

#Find the indexes where the values 2, 4, and 6 should be inserted:

var_array_6 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_8 = np.searchsorted(var_array_6, [1,5,7]) # 

print("\nSearch Multiple values")
print(var_search_8)

# The return value is an array: [ 0  4 11] containing the three indexes where 1,5,7 
# would be inserted in the original array to maintain the order.

# -------------------------
# Searching Multiple Values with right sided
var_array_6 = np.array([1,2,3,4,5,6,7,3,4,5,4])

var_search_8 = np.searchsorted(var_array_6, [1,5,7], side='right') # if not specified is left sided search

print("\nSearch Multiple values with right sided")
print(var_search_8)
print(sorted(var_array_6))
