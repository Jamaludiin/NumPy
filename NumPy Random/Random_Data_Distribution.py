# Random Data Distribution

"""
Data Distribution is a list of all possible values, and how often each value occurs.
Such lists are important when working with statistics and data science.
The random module offer methods that returns randomly generated data distributions.
"""

# Random Distribution
    # A random distribution is a set of random numbers that follow a certain probability density function.

# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

# We can generate random numbers based on defined probabilities using the choice() method of the random module.
    # The choice() method allows us to specify the probability for each value.
    # The choice() method allows you to generate a random value based on an array of values.
    # The choice() method takes an array as a parameter and randomly returns one of the values.

# The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.



from numpy import random

#-----------------------------------------------------------------------
# # consider this example
"""
    Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
    The probability for the value to be 3 is set to be 0.1
    The probability for the value to be 5 is set to be 0.3
    The probability for the value to be 7 is set to be 0.6
    The probability for the value to be 9 is set to be 0
"""
var_prob_random = random.choice([3,5,7,9], p=[0.3,0.4,0.2,0.1], size=(10)) # the probabilities must sum to 1

for i in var_prob_random:
 print(i)

print("\nPrint the sorted values of the generated random probability values")
print(sorted(var_prob_random)) # diffrent run diffrent values

# if some value's probability kept 0.0, it will never occur

#-----------------------------------------------------------------------
# Lets run Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
var_prob_random = random.choice([3,5,7,9], p=[0.3,0.4,0.2,0.1], size=(3,5)) # the probabilities must sum to 1

print("\nWith 2D arrays")
for i in var_prob_random:
 print(i)


#-----------------------------------------------------------------------
