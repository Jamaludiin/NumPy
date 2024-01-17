# Normal Distribution
"""
The Normal Distribution is one of the most important distributions.
It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------
var_normal_1 = random.normal(2,3) # diffrent run u will get diffrent result
var_normal_2 = random.normal(5,3)
var_normal_3 = random.normal(12,4)


print(var_normal_1)
print(var_normal_2)
print(var_normal_3)

# ------------------------------------------
# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:

var_normal_4 = random.normal(loc=1, scale=2, size=(2, 3))

print()
print(var_normal_4)

# or 
print()
for i in var_normal_4:
 print(i)

# ------------------------------------------
# Visualization of Normal Distribution

sns.distplot(random.normal(size=1000), hist=False)

plt.show()