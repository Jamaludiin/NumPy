# Zipf Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""Zipf distributions are used to sample data based on zipf's law.

Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

It has two parameters:
a - distribution parameter.
size - The shape of the returned array."""

# -----------------------------------------------------------------------------
var_zip_dis = random.zipf(a=3, size=3) # return three values

print(var_zip_dis)

# -----------------------------------------------------------------------------
# for loop the above values
print("\nFor loop")
for i in var_zip_dis:
    print(i)

# -----------------------------------------------------------------------------
var_zip_dis = random.zipf(a=3, size=(3, 3)) # return array with 3 by 3 values

print("\nAnother Size")
print(var_zip_dis)

# -----------------------------------------------------------------------------
# for loop the above values
print("\nFor loop")
for i in var_zip_dis:
    for k in i:
     print(k)
    
# -----------------------------------------------------------------------------
sns.distplot(var_zip_dis)
plt.show()

# -----------------------------------------------------------------------------
sns.distplot(random.zipf(a=2, size=1000), kde=False)

plt.show()

# -----------------------------------------------------------------------------
var_zip_dis = random.zipf(a=2, size=1000)
sns.distplot(var_zip_dis[var_zip_dis<10], kde=False)

plt.show()