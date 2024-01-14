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