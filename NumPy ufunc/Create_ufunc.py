"""
How To Create Your Own ufunc
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""
import numpy as np

# --------------------------------------------------------------------------
# Create your own ufunc for addition:

def fuc_add(x, y):
  return x+y

fuc_add = np.frompyfunc(fuc_add, 2, 1)


list1 = [1,2,3,4]
list2 = [5,6,7,8]

print(fuc_add(list1,list2))
# --------------------------------------------------------------------------

def fuc_sub(x, y):
  return x-y

def fuc_mult(x, y):
  return x*y

def fuc_div(x, y):
  return x/y


fuc_add = np.frompyfunc(fuc_add, 2, 1)
fuc_sub = np.frompyfunc(fuc_sub, 2, 1)
fuc_mult = np.frompyfunc(fuc_mult, 2, 1)
fuc_div = np.frompyfunc(fuc_mult, 2, 1)

print(fuc_sub(list1,list2))
print(fuc_mult(list1,list2))
print(fuc_div(list1,list2))

# --------------------------------------------------------------------------

