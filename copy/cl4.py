# Learning Methods / Commands

# String Commands / Methods
# str_var = "hello world this is my intro to world , so hello world"

# print(str_var.capitalize()) # Each word first letter is capital
# print(str_var.upper()) # Whole string is capital
# print(str_var.lower()) # whole string is lower
# print(str_var.__len__()) # length of the string
# print(str_var.split(" ")[0]) # prints first word of the string, " "(blank space) = delimiter
# print(str_var.replace("hello", "Bonjour")) # replaces "hello" in string with another substring "Bonjour"
# print(str_var.startswith("hell")) # checks whether the string starts with substring "hell"
# print(str_var.endswith("orld")) # checks whether the string ends with substring "orld"
# print(str_var[0].isalpha()) # checks if character is an alphabet
# Note: methods starting with "is" returns 'Boolean'

# List Commands / Methods
# list_var = [10, 9, 1, 2, 3.98]

# list_var[1] = 3 # changes the second element with "3"
# print(list_var)
# list_var.append(5) # adds to list at the end
# print(list_var)
# list_var.insert(2, 10) # adds to list at specific index, list_var.inset(index, element)
# print(list_var)

# print(list_var.__len__()) # lenght of the list

# list_var.sort() # sorts the string by default ascending order, returns none
# print(list_var)

# list_var.reverse() # reverse the string, returns none
# print(list_var)

# list_var.pop() # removes the last element, returns last element
# print(list_var)

# list_var.extend([5 , 6, 7]) # adds each element to list
# print(list_var)

# print(list_var.count(1)) # prints the count of a certain element

# print(list_var.index(10)) # finds the index of an element, will throw error

# Tuple Commands / Methods
# tuple_var = (1, 2, 3, 4, 5, 6,)

# tuple_var[0] = 4 # TypeError: 'tuple' object does not support item assignment

# Since tuple is immutable, only read operations can be done

# Set Commands / Methods
# set_1 = {1, 2, 2, 4, 4, 5, 5, 6, 7}
# set_2 = {5, 5, 6, 7, 7, 8, 8, 9, 0}

# # Union - All Combination of both sets
# print(f"Union: {set_1.union(set_2)}")

# # Intersection - Common between both sets
# print(f"Intersection: {set_1.intersection(set_2)}")

# # Difference - From one set to another set differences
# print(f"Set1 Difference Set2: {set_1.difference(set_2)}")
# print(f"Set2 Difference Set1: {set_2.difference(set_1)}")

# # Symmetric Difference - Difference from both the sets
# print(f"Symmetric Difference: {set_1.symmetric_difference(set_2)}")

# Dictionary Commands / Methods
# dict_var = {
#     "name": "yash",
#     "age": 21,
#     "course": "CSE"
# }


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

# dict_var.update({"course": "IT"}) # Updates the details in dictionary
# print(dict_var)

# dict_var.pop("course") # removes the "course" key: value pair
# print(dict_var)

# Learning Functions

# Functions are reusable block of code
# Declared with the keyword 'def'

# Syntax
"""
def function_name(parameters):
    code

function_name()
"""

# def sample(): # Declaration
#     print("Hello, World!") # Business Logic

# sample() # Calling Function

# passing parameters

# def sample(name):
#     print(f"Hello, {name}!")
# sample("Raj")

# def sample(name = "Karl"):
#     print(f"Hello, {name}!")
# sample()

# def sample(a, b):
#     print(f"Hello, {a+b}!")
# sample(2,5)

# def sample(*args): # 'args' is used to take n number of arguments, args: tuple
#     for i in args:
#         print(i)
# sample(1, 2, 3, 4, 5, 6, 7)

# def sample(**kwargs): # 'kwargs' keyword arguments, acts as dictionary, kwargs: dict[str, Any]
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# sample(name = "Yash", age = 21, isStudent = True)
