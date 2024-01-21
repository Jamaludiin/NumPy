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
var_fix = np.array([0.94039, 2.33, 0.123, 11.2, 34, -23.45, 0.0234])


print(np.trunc(var_truncate))
print(np.fix(var_truncate))
# produce same result
# ---------------------------------------------------------------------------
# Rounding
    # The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
    # E.g. round off to 1 decimal point, 3.16666 is 3.2