import numpy as np

"""
The np.arange function in NumPy is used to create an array with regularly spaced values within a specified range. It is similar to the built-in range function in Python but returns a NumPy array.

Here is the syntax of np.arange:

    numpy.arange([start, ]stop, [step, ]dtype=None)
    
    start: The start of the interval. If not specified, it defaults to 0.
    stop: The end of the interval (exclusive).
    step: Spacing between values. If not specified, it defaults to 1.
    dtype: The data type of the output array. If not specified, it inherits the data type from the input values.

"""

import numpy as np

# Here are some examples of using np.arange:

# Example 1: Default start and step
arr1 = np.arange(5)  # Output: [0, 1, 2, 3, 4]
print(arr1)

# Example 2: Specifying start,and stop
arr2 = np.arange(2, 10)  # Output: [2, 3, 4, 5, 6, 8, 9]
print(arr2)

# Example 2: Specifying start, stop, and step
arr2 = np.arange(2, 10, 2)  # Output: [2, 4, 6, 8]
print(arr2)

# Example 3: Specifying dtype
arr3 = np.arange(0, 1, 0.1, dtype=float)  # Output: [0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
print(arr3)

# Example 4: Using a negative step
arr4 = np.arange(10, 0, -1)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(arr4)
