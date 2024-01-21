# Rounding Decimals
import numpy as np

"""
Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

    truncation
    fix
    rounding
    floor
    ceil
"""

# ---------------------------------------------------------------------------
# Truncation
    # Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

var_truncate = np.array([0.94039, 2.33, 0.123, 11.2, 34, -23.45, 0.0234])

print(np.trunc(var_truncate))
print(np.fix(var_truncate))
# produce same result
# ---------------------------------------------------------------------------
# Rounding
    # The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
    # E.g. round off to 1 decimal point, 3.16666 is 3.2

var_round = np.array([0.94039, 2.78, 0.123, 11.2, 34, -23.45, 0.0234])

print("\nRounding no spceifed the second argument")
print(np.round(var_round))
print("\nRounding spceifed the second argument")
print(np.round(3.1666,  2))
print(np.round(np.array([3.1666,3.467,12.338]),  2))
print(np.round([3.1666,3.467,12.338],  2)) # same the above

# ---------------------------------------------------------------------------
# Floor
    # The floor() function rounds off decimal to nearest lower integer.
    # E.g. floor of 3.166 is 3.
print("\nRounding using the floor method")
print(np.floor([3.1666,3.467,12.338]))


# Ceil
    # The ceil() function rounds off decimal to nearest upper integer.
    # E.g. ceil of 3.166 is 4.

print("\nRounding using the ceil method")
print(np.ceil([3.1666,3.467,12.338]))