# NumPy Logs

"""Logs
NumPy provides functions to perform log at the base 2, e and 10.

We will also explore how we can take log for any base by creating a custom ufunc.

All of the log functions will place -inf or inf in the elements if the log can not be computed."""

from math import log
import numpy as np

# ---------------------------------------------------------------------------
# Log at Base 2
# Use the log2() function to perform log at the base 2.

# Find log at base 2 of all elements of following array:
var_log_base_2 = np.arange(1, 10)

print(np.log2(var_log_base_2))

# ------------------------
# for loop
print()
for i in np.log2(var_log_base_2):
    print(i)

# ---------------------------------------------------------------------------
# for loop but rownded
print("\nfor loop but rownded")
for i in np.floor(np.log2(var_log_base_2)):
    print(i)

# ---------------------------------------------------------------------------
# Log at Base 10
    # Use the log10() function to perform log at the base 10.

# Find log at base 10 of all elements of following array:
print("\nLog base 10 no loop no round")

var_log_base_10 = np.arange(1, 10)

print(np.log10(var_log_base_10))

# ------------------------
# for loop
print("\nLog base 10 for loop but rownded 3 digit")
for i in np.round(np.log10(var_log_base_10),3):
    print(i)

# ---------------------------------------------------------------------------
# Natural Log, or Log at Base e
    # Use the log() function to perform log at the base e.

print("\nNatural Log, or Log at Base e no loop no round")

var_log_base_e = np.arange(1, 10)

print(np.log(var_log_base_e))

# ------------------------
# for loop
print("\nNatural Log base e for loop but rownded 3 digit")
for i in np.round(np.log(var_log_base_e),3):
    print(i)

# ---------------------------------------------------------------------------
# Log at Any Base
    # NumPy does not provide any function to take log at any base, so we can use the frompyfunc() 
    # function along with inbuilt function math.log() with two input parameters and one output parameter:
print("\nLog at Any Base")

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))