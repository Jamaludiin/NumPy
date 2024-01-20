# Rayleigh Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
Rayleigh distribution is used in signal processing.

It has two parameters:
scale - (standard deviation) decides how flat the distribution will be default 1.0).
size - The shape of the returned array.
"""
# -----------------------------------------------------------------------------
var_ray_dist = random.rayleigh(scale=2, size=3)

print(var_ray_dist)

# -----------------------------------------------------------------------------
print("\nFor Lopp")
for i in var_ray_dist:
    print(i)

# -----------------------------------------------------------------------------
var_ray_dist = random.rayleigh(scale=2, size=(3,4))

print()
print(var_ray_dist)

# -----------------------------------------------------------------------------
print("\nFor Lopp with size array")
for i in var_ray_dist:
    for k in i:
     print(k)

# -----------------------------------------------------------------------------
# visualize 
sns.distplot(var_ray_dist)
plt.show()

# -----------------------------------------------------------------------------
# Similarity Between Rayleigh and Chi Square Distribution
# At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions.

sns.distplot(var_ray_dist, hist=False, label="Rayleigh")
sns.distplot(random.chisquare(df=3, size=(3, 3)), hist=False, label="ChirSquare")

plt.show()