# What is a Random Number?
    # Random number does NOT mean a different number every time. 
    # Random means something that can not be predicted logically.

# Pseudo Random and True Random.
    # So it means there must be some algorithm to generate a random number as well.
    # If there is a program to generate random number it can be predicted, thus it is not truly random

    # Random numbers generated through a generation algorithm are called pseudo random.

# an we make truly random numbers?
    # Yes. In order to generate a truly random number on our computers we need to get the random data from some 
      # outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
    # We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or the basis 
      # of application is the randomness (e.g. Digital roulette wheels).
# source w3schools.com

from numpy import random
# ---------------------------------
# Generate Random Number
    # NumPy offers the random module to work with random numbers.

var_random = random.randint(100)

print(var_random)

# ---------------------------------
# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.

var_random_float = random.rand()

print("\nRnadom float from 0 - 1 using rand() method")
print(var_random_float)

# ---------------------------------
# The rand() method also allows you to specify the shape of the array.
# Generate a 1-D array containing 5 random floats:
var_random_float = random.rand(6)

print("\nGenerate a 1-D array containing 6 random floats:")
print(var_random_float)

print("\nLooping the values")

for i in var_random_float:
    print(var_random_float) # or call i for one by one


# ---------------------------------
# Generate a 1-D array containing 5 random integers from 0 to 100:
var_random_1 = random.randint(100, size=5)

print("\nGenerate a 1-D array containing 5 random integers from 0 to 100:")
print(var_random_1)

# ---------------------------------
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
var_random_2 = random.randint(100, size=(3,5))

print("\nGenerate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:")
print(var_random_2)

# ---------------------------------
# Generate a 2-D array with 3 rows, each row containing 5 random numbers:

var_random_3 = random.rand(3, 5)

print("\nGenerate a 2-D array with 3 rows, each row containing 5 random numbers:")
print(var_random_3)

# ---------------------------------
# Generate Random Number From Array
    # The choice() method allows you to generate a random value based on an array of values.
    # The choice() method takes an array as a parameter and randomly returns one of the values.

var_random_4 = random.choice([2,3,7,8,9,4])

print("\nGenerate Random Number From Array")
print(var_random_4)

# ---------------------------------
# Generate a 2-D array that consists of the values in the array parameter [2,3,7,8,9,4]:
var_random_4 = random.choice([2,3,7,8,9,4],size=(3,5))

print("\nGenerate a 2-D array that consists of the values in the array parameter [2,3,7,8,9,4]:")
print(var_random_4)
