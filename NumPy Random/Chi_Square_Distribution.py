# Chi Square Distribution
"""
Chi Square distribution is used as a basis to verify the hypothesis.

It has two parameters:
df - (degree of freedom).
size - The shape of the returned array.
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
var_chi_dis = random.chisquare(df=3, size=3) # return three values

print(var_chi_dis)

# -----------------------------------------------------------------------------
# for loop the above values
print("\nFor loop")
for i in var_chi_dis:
    print(i)

# -----------------------------------------------------------------------------
var_chi_dis = random.chisquare(df=3, size=(3, 3)) # return array with 3 by 3 values

print("\nAnother Size")
print(var_chi_dis)

# -----------------------------------------------------------------------------
# for loop the above values
print("\nFor loop")
for i in var_chi_dis:
    for k in i:
     print(k)
    
# -----------------------------------------------------------------------------
sns.distplot(var_chi_dis)
plt.show()

# -----------------------------------------------------------------------------
