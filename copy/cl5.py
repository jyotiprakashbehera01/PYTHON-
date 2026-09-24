# Exception Handling
# Managing unexpected errors at runtime so that the code doesn't break

# Components of Exception Handling
# try -> Contains Business Logic
# except -> Handle exceptions of business logic(try)
# else -> If no exception occurs
# finally -> No-matter what, it gets executed

# syntax
# try:
#     business logic
# except:
#     exception while business logic
# else:
#     no error
# finally:
#     no matter what finally gets executed

# types of exceptions
# 1. Built-in Exceptions: Exceptions which are already present in python, such as(ValueError, TypeError, KeyError, ZeroDivisionError)
# 2. Custom Exceptions: Exceptions built by the developer, such as(InsufficientFundsError)

# try:
#     num = int(input("Enter a number: "))
#     res = num/0
#     print(res)
# except ZeroDivisionError:
#     print("Number can't be divided by zero")

# try:
#     data = [10, 20]
#     res = data[5] / 0
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except IndexError:
#     print("Index is out of range")
# except(TypeError, ValueError, NameError) as Error:
#     print(Error)

# try:
#     num = int(input("Enter a number: "))
#     res = 100 / num
# except(ZeroDivisionError, TypeError, ValueError) as e:
#     print(e)
# else:
#     print(f"Success: {res}")
# finally:
#     print("No matter what finally is getting executed")

# Manually 'raise' the error
# age = -3
# try:
#     if age < 0:
#         raise ValueError("Age cannot be less than zero")
# except ValueError as e:
#     print(e)

# Comprehension

# List Comprehension

# list_var = [1, 2, 3, 4, 5, 6, 7]

# squares = [x**2 for x in list_var if x % 2 == 0]
'''
squares = []
for x in list_var:
    if x % 2 == 0:
        squares.append(x**2)
'''
# print(squares) # output is a new list

# Dictionary Comprehension
# list_var = ["Apple", "Banana", "Carrot", "DragonFruit", "EggPlant"]
# dict_var = {word:len(word) for word in list_var}
# print(dict_var)

# Set Comprehension
# list_var = ["Virat", "VIRAT", "Yash", "Raj", "RAJ"]
# set_var = {name.lower() for name in list_var}
# print(set_var)

# lambda -> small and anonymous functions

# syntax
# lambda arguments: expression

# double = lambda x: x * 2 # in-line function
# print(double(5))

# map function: it transforms every item

# syntax
# map(function,iterable)

# list_var = [1, 2, 3, 4]

# double = list(map(lambda x : x * 2, list_var))
# print(double)

# filter function: it filters all the records

# syntax
# filter(function, iterable)

# list_var = [1, 2, 3, 4]

# filtered_record_even = list(filter(lambda x : x % 2 == 0, list_var))
# print(filtered_record_even)

# reduce: running total
# from functools import reduce
# list_var = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, list_var)
# print(product)