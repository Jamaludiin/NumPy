from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------
# Uniform Distribution
"""
Used to describe probability where every event has equal chances of occuring.
E.g. Generation of random numbers.

It has three parameters:

a - lower bound - default 0 .0.
b - upper bound - default 1.0.
size - The shape of the returned array.
"""

var_uni_dist = random.uniform(size=10)

print(var_uni_dist)

# or print through loop
print("\nLooping the values")
k = 1
for i in var_uni_dist:
    print(k, "-:",i)
    k +=1

# -----------------------------------------------------------
# ploting the uniform distribution
sns.distplot(var_uni_dist, hist=False)

plt.show()

# -----------------------------------------------------------
