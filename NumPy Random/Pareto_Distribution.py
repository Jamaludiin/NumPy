# Pareto Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

It has two parameter:

a - shape parameter.
size - The shape of the returned array."""
# -----------------------------------------------------------------------------
var_pareto_dis = random.pareto(a=3, size=3) # return three values

print(var_pareto_dis)

# -----------------------------------------------------------------------------
# for loop the above values
print("\nFor loop")
for i in var_pareto_dis:
    print(i)

# -----------------------------------------------------------------------------
var_pareto_dis = random.pareto(a=3, size=(3, 3)) # return array with 3 by 3 values

print("\nAnother Size")
print(var_pareto_dis)

# -----------------------------------------------------------------------------
# for loop the above values
print("\nFor loop")
for i in var_pareto_dis:
    for k in i:
     print(k)
    
# -----------------------------------------------------------------------------
sns.distplot(var_pareto_dis)
plt.show()

# -----------------------------------------------------------------------------
