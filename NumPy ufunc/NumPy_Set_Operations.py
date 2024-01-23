# NumPy Set Operations
import numpy as np

# --------------------------------------------------------------------------
# What is a Set
    # A set in mathematics is a collection of unique elements.
    # Sets are used for operations involving frequent intersection, union and difference operations.

# --------------------------------------------------------------------------
# Create Sets in NumPy
    # We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

# Convert following array with repeated elements to a set:
var_array = np.array([1,2,4,5,6,7,3,7,8,9,2,8,6])

var_unique = np.unique(var_array)

print("Unique values in the array")
print(var_unique)
print(type(var_unique))

# --------------------------------------------------------------------------
# Finding Union
    # To find the unique values of two arrays, use the union1d() method.

var_array_1 = np.array([1,2,4,5,6,7,3])
var_array_2 = np.array([7,8,9,2,8,6,5])

var_Union = np.union1d(var_array_1, var_array_2)

print("\nUnion values in the arrays")
print(var_Union)

# --------------------------------------------------------------------------
# Finding Intersection
    # To find only the values that are present in both arrays, use the intersect1d() method.

var_Union = np.intersect1d(var_array_1, var_array_2, assume_unique=True) # is optional to mention this assume_unique=True

print("\nFinding Intersection values in the arrays")
print(var_Union)

# --------------------------------------------------------------------------
# Finding Difference
    # To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
var_Difference= np.setdiff1d(var_array_1, var_array_2, assume_unique=True) # is optional to mention this assume_unique=True

print("\nFinding Difference values in the arrays")
print(var_Difference)

# --------------- same but 
var_Difference= np.setdiff1d(var_array_2, var_array_1, assume_unique=True) # find the var_array_2, var_array_1, instead of var_array_1, var_array_2,

print("\nFinding Difference values in the arrays")
print(var_Difference)

# --------------------------------------------------------------------------
# Finding Symmetric Difference
    # To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
var_Symmetric_Difference= np.setxor1d(var_array_1, var_array_2, assume_unique=True) 

print("\nFinding Symmetric Difference values in the arrays")
print(var_Symmetric_Difference)