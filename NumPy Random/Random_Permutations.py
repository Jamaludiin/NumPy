# Random Permutations of Elements
"""
    A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
    The NumPy Random module provides two methods for this: shuffle() and permutation().
"""


# Shuffling Arrays
    # Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

from numpy import random
import numpy as np

# --------------------------------------------------------------------
var_array_1 = np.array([1,2,3,4,5,6,7,8,9])

random.shuffle(var_array_1) # randomly shufles, every run diffrent order

print(var_array_1)

print(random.shuffle(var_array_1)) # this code will not return anything or IT MEANS THE VALUES ARE SHUFLED IN THE VARIABLE
                                   # The shuffle() method makes changes to the original array.

# --------------------------------------------------------------------
# what about this example 
var_array_1 = np.array([3,5,7,9])

random.shuffle(var_array_1) # randomly shufles, every run diffrent order
var_prob_random = random.choice(var_array_1, p=[0.3,0.5,0.2,0.0], size=(10))
var_prob_random_no_shufle = random.choice([3,5,7,9], p=[0.3,0.5,0.2,0.0], size=(10))


# shufled values
print("\nshufled values")
print(var_array_1)
print("\nProbaility generated from shufled values")
print(var_prob_random)
print("\nProbaility generated withou shufled values")
print(var_prob_random_no_shufle)


# --------------------------------------------------------------------
# Generating Permutation of Arrays
# Generate a random permutation of elements of following array:

var_array_2 = np.array([1,4,7,9,6])

# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
random.permutation(var_array_2) # DOES NOT MAKE ANY SENSE

print("\nGenerate a random permutation of elements of following array: does not change the original")
print(var_array_2)

print("\nGenerate a random permutation of elements of following array:")
print(random.permutation(var_array_2)) # this is correct way becouse unlike the previous shufle 
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).

# --------------------------------------------------------------------
