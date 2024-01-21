# Simple Arithmetic
import numpy as np

var_array_1 = np.array([10, 11, 12, 13, 14, 15])
var_array_2 = np.array([20, 21, 22, 23, 24, 25])
# --------------------------------------------------------------------------

# Addition
    # The add() function sums the content of two arrays, and return the results in a new array
var_add = np.add(var_array_1, var_array_2)

# Subtraction
    # The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.
var_subtract = np.subtract(var_array_1, var_array_2)

# Multiplication
    # The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.
var_multiply = np.multiply(var_array_1, var_array_2)

# Division
    # The divide() function divides the values from one array with the values from another array, and return the results in a new array.
var_divide = np.divide(var_array_1, var_array_2)

# Power
    # The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.
var_power = np.power(var_array_1, var_array_2)

# Remainder
    # Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.
    # You get the same result when using the remainder() function:
var_mod = np.mod(var_array_1, var_array_2)
var_remainder = np.remainder(var_array_1, var_array_2)

# Quotient and Mod
    # The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
var_divmod = np.divmod(var_array_1, var_array_2)

# Absolute Values
    # Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()
var_absolute = np.absolute(var_array_1, var_array_2)


# output all

print("\nThis is Add")
print(var_add)
print("\nThis is Subtraction")
print(var_subtract)
print("\nThis is Multiply")
print(var_multiply)
print("\nThis is Divide")
print(var_divide)
print("\nThis is Power")
print(var_power)
print("\nThis is Reminder but mod")
print(var_mod)
print("\nThis is Reminder but Reminder")
print(var_remainder)
print("\nThis is Divmod")
print(var_divmod)
print("\nThis is Absolute")
print(var_absolute)






