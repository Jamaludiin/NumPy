# NumPy Data Types
"""
Apart from the Python normal data types, NumPy also has some other or aditional data types

Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
 source: w3schools.com

"""
import numpy as np

# ----------------------------------------------------------------------------
# lets first Check the Data Type of an Array
# use the dtype, it returns the data type of the array

var_array_1 = np.array([1,2,3,4,5,6,7,8])
var_array_2 = np.array([1,2,3,4,5,6,"3","rtt",True])
var_array_3 = np.array(["1,2,3,4,5,6,""3","rtt","ert","tyui"])
var_array_4 = np.array(["1,2,3,4,5,6,","3","rtt","ert","tyui"])



# dtype, no need to pass argument or value
print(var_array_1.dtype) # returns int or int64
print(var_array_2.dtype) # returns U - unicode string
print(var_array_3.dtype) # returns U - unicode string
print(var_array_4.dtype) # returns U - unicode string

print()
# --------------------------
# check array size
print(len(var_array_1), var_array_1.dtype)
print(len(var_array_2), var_array_2.dtype)
print(len(var_array_3), var_array_3.dtype)
print(len(var_array_4), var_array_4.dtype)


print()
# ----------------------------------------------------------------------------
# Lets create an arrays With a pre-defined Data Type
# remember we used to create arrays using array() function this also same but additionally 
    # we add argument using dtype = 'the datatype as sympols indicated above'

var_array_5 = np.array([1,2,3,4,5,6,7,8], dtype='U')
print(var_array_5.dtype) # returns U - unicode string

var_array_6 = np.array([1,2,3,4,5,6,7,8], dtype='i')
print(var_array_6.dtype) # returns U - unicode string


print()
# -------------------------------
# For i, u, f, S and U we can define size as well.

var_array_7 = np.array([1,2,3,4,5,6,7,8,9], dtype='i1') # it accept i1, i4, i8 but other numbers refused, becouse he use byte based measure
print(var_array_7.dtype) # int8 bit
print(var_array_7) 

var_array_8 = np.array([1,2,3,4,5,6,7,8,9], dtype='i4') 
print(var_array_8.dtype) # int32 bit
print(var_array_8)

var_array_9 = np.array([1,2,3,4,5,6,7,8,9], dtype='i8') 
print(var_array_9.dtype) # int64 bit
print(var_array_9)


print()
# ----------------------------------------------------------------------------
# remember, some values can be to converted to each other such as 1,2,3 int numbers to string such as
var_array_10 = np.array([1,2,3,4,5,6,7,8,9], dtype='S') 
print(var_array_10.dtype) # S1 bit
print(var_array_10)

# while others canot such as "w","1","4","4" they are string but cannot be converted to int becouse some are string
# this code will be an error 
"""var_array_11 = np.array(["1","2","3","4","a","r","t","8","9"], dtype='i') 
print(var_array_11.dtype) # S1 bit
print(var_array_11)"""

#----------------------------
# convert float to int
var_array_12 = np.array([1.5,2.3,3.7,4.8,5.9,6.1,7.33,8,9]) 
print(var_array_12.dtype) # float64 bit
print(var_array_12)

print()

# var_array_12.dtype='i'        this is not proper type
var_array_12 = np.array([1.5,2.3,3.7,4.8,5.9,6.1,7.33,8,9],dtype='i') 
print(var_array_12.dtype) # int32 bit, all float points are ignored, please take care, you might loose data
print(var_array_12)