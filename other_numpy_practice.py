import numpy as np

var_array = np.array([1,2,3,4,5,6,2,7])

for i in var_array:
    if i == 2:
     print(i)
    else:
       print("not found")


# -------------------------
print("\nAnother search-------------------------^")
var_array = np.array([1,2,3,4,5,6,2,7])

for i in var_array:
    if i == 2:
     print(i)
     break
    else:
       print("not found")

# -------------------------
# searching duplicate value of 2 and stre them in a value
print("\nAnother search-------------------------^")
var_array = np.array([1,2,3,4,5,6,2,7])

var_value = []
for i in var_array:
    if i == 2:
     var_value.append(i)

print(var_value)

# -------------------------
# print with their index as well
print("\nAnother search-------------------------^")
var_array = np.array([1,2,3,4,5,6,2,7])

var_value = []
index_val = []
for k, i in np.ndenumerate(var_array):
    if i == 2:
     var_value.append(i)
     index_val.append(k)

print("the values are :",var_value, "and their respective index are :",index_val)

# ----------------------------
# print and collect only duplicates 
var_array = np.array([1, 2, 3, 4, 5, 3, 6, 2, 4, 7, 6])
var_duplicates = set()
var_collected_duplicates = []

print()
for i in var_array:
    if i in var_duplicates:
        var_collected_duplicates.append(i)
        print("Duplicate found:", i)
    else:
        var_duplicates.add(i)

print("Collected duplicates:", var_collected_duplicates)


print()
# --------------------
var_array = np.array([1, 2, 3, 4, 5, 3, 6, 2, 4, 7, 6])
var_duplicate_occurrences = {}

for i in var_array:
    if i in var_duplicate_occurrences:
        var_duplicate_occurrences[i].append(i)
    else:
        var_duplicate_occurrences[i] = [i]

# Filter duplicates that occurred more than once and print them
for key, occurrences in var_duplicate_occurrences.items():
    if len(occurrences) > 1:
        print(f"Duplicates of {key}: {occurrences}")


# ---------------------------------
var_array_1 = np.array([1, 2, 3, 4, 5, 3, 3, 6, 2, 4, 7, 6])

var_duplicate_1 = []
var_duplicate_2 = []
for i in var_array_1:
    if i in var_duplicate_2:
        var_duplicate_1.append(i)
    else:
        var_duplicate_2.append(i)


print("\nduplicate evaluation")
print("duplicate values :",var_duplicate_1)
print("unique values extracted :",var_duplicate_2)

