# Comments -> Things which doesn't execute in the program. It is used to explain the code and make it more readable.
# We have single line comment (Denoted by #)
"""
Multi
line
comments
are denoted by (""" """)
"""

# Variables (Stored in local memory)
# Python is dynamically typed - Datatypes are automatically declared at runtime

# camelCase -> usually used in java
# lower_case -> functions, variables
# Pascal_Case -> classes
# UPPER_CASE -> constants

str_var = "Hello, World!"  # Collection of Characters
int_var = 21  # Whole Number
float_var = 9.18  # Decimal Number
bool_var = True  # True or False
dict_var = {"name": "Raj", "age": 21, "isCool": True}  # Key: Value Pairs
list_var = [
    1,
    2,
    2,
    3,
    "Hello ",
    5,
    True,
    7.001,
    8,
    9,
]  # Heterogeneous Elements(memory is dynamically allocated)
# Accepts Duplicate Values, Mutable, Ordered
tuple_var = (1, 2, 3, 4, 5, 5, 6)  # Immutable
set_var = {1, 2, 2, 3, 4, 4, 5}  # Unique and unordered collection of items

# Arrays in Python
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])# 1 * 6 # 1D Array
# mat = np.array([1, 2, 3],[4, 5, 6])# 2 * 3 # 2D Array

# print() function - To Display Output

# print(str_var + int_var) # TypeError: can only concatenate str (not "int") to str

# print(str_var + str(int_var)) # Type Casting

# print(f"{}") function - Fromatted print()

# print(f"{str_var} {int_var}")

# Input from user

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# Dictionary Methods
# print(dict_var)
# print(dict_var.keys())
# print(dict_var.values())
# print(dict_var.items()) # keys and values as well

# for key, value in dict_var.items():
#     print(f"{key} : {value}")

# print(dict_var.get("name")) # Exception handling, returns None
# print(dict_var["name"]) # KeyError

# print(dict_var.get("address")) # None
# print(dict_var["address"]) # KeyError: 'address'

# Set functions
set_1 = {1, 2, 3, 4, 5}
set_2 = {5, 6, 7, 8, 9}

# Union - All Combination of both sets
# print(f"Union: {set_1.union(set_2)}")

# Intersection - Common between both sets
# print(f"Intersection: {set_1.intersection(set_2)}")

# Difference - From one set to another set differences
# print(f"Set1 Difference Set2: {set_1.difference(set_2)}")
# print(f"Set2 Difference Set1: {set_2.difference(set_1)}")

# Symmetric Difference - Difference from both the sets
# print(f"Symmetric Difference: {set_1.symmetric_difference(set_2)}")
