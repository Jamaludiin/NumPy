# Poisson Distribution
"""
Poisson Distribution is a Discrete Distribution.
It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.
size - The shape of the returned array.
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
# Generate a random 1x10 distribution for occurrence 2:

var_poisson_distri = random.poisson(lam=2,size=10)

print(var_poisson_distri)

# -----------------------------------------------------------------------------
# or 
var_poisson_distri_1 = random.poisson(lam=2,size=(10, 10))

print()
print(var_poisson_distri_1)

# -----------------------------------------------------------------------------
print("\nLooping the dimentions")
for i in var_poisson_distri_1:
    print(i)

# -----------------------------------------------------------------------------
# Visualization of Poisson Distribution
sns.distplot(var_poisson_distri_1)
plt.show()

# another
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

# -----------------------------------------------------------------------------
# Difference Between Normal and Poisson Distribution
"""Normal distribution is continuous whereas poisson is discrete.

But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal 
distribution with certain std dev and mean."""