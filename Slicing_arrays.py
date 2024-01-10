"""
                                    Slicing arrays
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].

    If we don't pass start its considered 0
    If we don't pass end its considered length of array in that dimension
    If we don't pass step its considered 1
        
        cite text: source: w3schools.com
"""

import numpy as np


var_array_1 = np.array([1,2,3,4,5,6,7,8,9])

# slicing using positive indexing
#-------------------------------------------
print("\nPostive indexing or Positive Range Indexing\n")
print(var_array_1[1:3])
# not specified the end of the index, thus, it will go up to the last index
print(var_array_1[1:])
# not specified the first index, while the last index is being called the length of the variable it self
print(var_array_1[:len(var_array_1)])


# slicing using Negative Indexing
#-------------------------------------------
# Negative indexing starts from the last element with index -1 and goes in reverse order.
print("\nNegative indexing or Negative Range Indexing\n")
print("the last elemnt",var_array_1[-1:]) # the last elemnt
print("except the last elemnt",var_array_1[:-1]) # except the last elemnt
print("except the last elemnt",var_array_1[0:-1]) # except the last elemnt, same the above one

print("nothing will be printed",var_array_1[-1:-1]) # nothing will be printed, becouse, they are arguing to print last element and except last element
print("starting the last 5th elemnt to front",var_array_1[0:-5]) # start the 5sth counting from back to front

print("start the 5sth counting except the last element",var_array_1[-5:-1]) # start the 5sth counting except the last element

# slicing to extract specific subsets from a array. Positive values only for now
#-------------------------------------------
print("\nSlice every other values in the set",var_array_1[::2])
print("Slice every other values in the set but start at midel",var_array_1[int(len(var_array_1)/2)::2])

# slicing to extract specific subsets from a array. Negative values only for now
#-------------------------------------------
print("\nSlice every other values in the set BUT REVERSE WAY",var_array_1[::-2])
print("Slice BY REVERSING THE VALUES ORDER",var_array_1[::-1])
print("Slice every other values in the set but start at -5",var_array_1[-5::2])

# indexing and slicing is diffrent [:] or [::] but indexing only use [] or [,] if its dimention based

# ------------------------------------------------------------------------------------------------------
# SLICING TWO DIMENTIONAL ARRAY
var_array_2 = np.array([[1,2,3,4],[5,6,7,8]])

# slicing multi dimentional array using positive indexing
#-------------------------------------------
print("\nSlicing 2D arrays",var_array_2[1, 1:4]) # second row values ranging from the second position to third position
print("\nSlicing 2D arrays",var_array_2[0, 0:]) # first row values ranging from the first position to last position

# target both array dimentions and return specific value from both
print("\nSlicing 2D arrays",var_array_2[0:2, 2]) # this means array 0 and 1 is targeted the 2 will be execluded, then the third element from both rows is targeted
print("\nSlicing 2D arrays",var_array_2[0:2, 0:3]) # the second 0:3 targets the values if this range in the sets 0:2

# slicing multi dimentional array using negative indexing
#-------------------------------------------
print("\nSlicing 2D arrays: row 2 or dimention 2 and their last elements",var_array_2[1, -1:]) # row 2 or dimention 2 and their elements ranging from 1 to 3
print("Slicing 2D arrays return all emelents in second dimention except the last",var_array_2[1, :-1])# return all emelents in second dimention except the last