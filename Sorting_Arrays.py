# Sorting Arrays

import numpy as np

var_array_1 = np.array(['banana', "tiger",'cherry', 'apple',"car","lion"])
var_array_2 = np.array([1,2,3,4,5,6,7,3,4,5,4])

# using sort() method
print("\nSort string in numpy")
print(np.sort(var_array_1))

print("\nSort numbers in numpy")
print(np.sort(var_array_2))


print("\nSorted() numbers without numpy") 
print(sorted(var_array_2))

# this one only tells you where to be put the 8 value
print("\np.searchsorted() numbers without numpy") 
sorted_array = np.searchsorted(var_array_2,8)
print(sorted_array)


# ---------------------------
# sorting multidimentional array
var_array_2 = np.array([[[1, 3, 2], [18, 17, 16], [6, 4, 5], [9, 7, 8], [15, 13, 14], [11, 10, 12]]])
var_sort_4 = np.sort(var_array_2) # If you use the sort() method on a 2-D array, both arrays will be sorted:

print(var_sort_4)