# Exponential Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
"""Exponential distribution is used for describing time till next event e.g. failure/success etc.

It has two parameters:
scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
size - The shape of the returned array.
"""

# Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:

var_exp_dis = random.exponential(scale=2, size=3)

print(var_exp_dis)

# -----------------------------------------------------------------------------
# for loop
print("\nUsing for loop")
for i in var_exp_dis:
    print(i)

# -----------------------------------------------------------------------------
var_exp_dis = random.exponential(scale=2, size=(2,3)) # return array

print(var_exp_dis)

# -----------------------------------------------------------------------------
# for loop
print("\nUsing for loop")
for i in var_exp_dis:
    for k in i:
      print(k)

# -----------------------------------------------------------------------------
# Visualization of Exponential Distribution
sns.distplot(var_exp_dis) # u can disable the hist=False

plt.show()

# -----------------------------------------------------------------------------
# Relation Between Poisson and Exponential Distribution
# Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.
var_exp_dis = random.exponential(scale=2, size=(2,3))
var_pois_dis = random.poisson(lam=2,size=(2,3))

sns.distplot(var_exp_dis, hist=False, label="Exponential")
sns.distplot(var_pois_dis, hist=False, label="Poisson")

plt.show()