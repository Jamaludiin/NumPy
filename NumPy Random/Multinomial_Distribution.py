# Multinomial Distribution
"""
Multinomial distribution is a generalization of binomial distribution.
It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

It has three parameters:

n - number of possible outcomes (e.g. 6 for dice roll).
pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------
var_multinomial = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(var_multinomial)

"""
Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.

Note: As they are generalization of binomial distribution their visual representation and similarity of normal 
      distribution is same as that of multiple binomial distributions.
"""
# -----------------------------------------------------------
# looping the values and printing one by one
print("\nLooping")
for i in var_multinomial:
    print(i)
# -----------------------------------------------------------
print("\nWith size attribute")
var_multinomial = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(2,3))

print(var_multinomial)

# -----------------------------------------------------------
# looping the values and printing one by one
print("\nLooping")
for i in var_multinomial:
    for k in i:
     print(k)

# -----------------------------------------------------------
# ploting the Multinomial Distribution

sns.distplot(var_multinomial)
plt.show()

sns.distplot(var_multinomial, hist=False)
plt.show()

