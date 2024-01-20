# What are ufuncs?
# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.

"""
Why use ufuncs?
    ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
    They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

ufuncs also take additional arguments, like:
    where: boolean array or condition defining where the operations should take place.
    dtype: defining the return type of elements.
    out: output array where the return value should be copied.
"""

"""
What is Vectorization?
    Converting iterative statements into a vector based operation is called vectorization.
    It is faster as modern CPUs are optimized for such operations."""

import numpy as np

# Add the Elements of Two Lists
    # list 1: [1, 2, 3, 4]
    # list 2: [4, 5, 6, 7]
    # One way of doing it is to iterate over both of the lists and then sum each elements.

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
result = []
for i in range(len(list1)):
    result.append([list1[i] + list2[i]])

print(list1)
print(list2)
print("\nUsing the normal python loop")
print(result)

# ---------------------------------------------------------------------------
# lets use the zip method
# One way of doing it is to iterate over both of the lists and then sum each elements.

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
result = []

# Without ufunc, we can use Python's built-in zip() method:
for i, j in zip(list1, list2):
    result.append(i + j)

print("\nUsing the Zip method")
print(result)


# ---------------------------------------------------------------------------
# NumPy has a ufunc for this, called add(x, y) that will produce the same result.

print("\nUsing the add(x, y) method in NumPy")

result = np.add(list1,list2)
print(result)

# ---------------------------------------------------------------------------
# print("\nUsing the add(x, y) method in NumPy")

list3 = [4, 5, 6, 7]
list4 = [4, 5, 6, 7]

"""result = np.add(list1,list2,list4) # you cannot use more than three parameters but if three has to be arraytype
print(result)"""

# ---------------------------------------------------------------------------
# Solution of the above 
list3 = [1, 1, 1, 1]

# Convert lists to NumPy arrays
arr1 = np.array([[1, 2, 3, 4], [8, 9, 5, 7]])
arr2 = np.array(list3)

# Use np.add to add two arrays element-wise
result = np.add(arr1, arr2) # add list 3 in each row of the arr1

print("\nUsing the add(x, y) method in NumPy array parameters")
print(result)

# ---------------------------------------------------------------------------
