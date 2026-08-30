# FUNCTION :

# -->It is a reuseable block of code that perform a specific task .
# -->It can write it once inside a function and call it whenever we need it.
# -->def → keyword used to create a function
# function_name → name of the function
# () → parameters go inside these parentheses
# : → starts the function body .


# def add(a, b):
#     return a + b


# result = add(10, 20)
# print(result)

# 1.PARAMETER :
# -->parameter are the variable writen inside the function defination ,
# -->It is a place holder that receives a value .
# --> upper a , b are the parameter .

# 2.ARGUMENT :
# -->Argument is the actual value that passed when calling the function .
# -->In upper 10 ,20 are the argument .


# 3.RETURN :
# -->Return send a value back from function .
# def Square(num):
#     return num * num


# result = Square(5)
# print(result)


# RETURN vs PRINT
# ->PRINT = it has disply the result but not return .
# ->RETURN = it has give the result back so we can store or used it .


# 4.DEFULT ARGUMENT :
# -->A parameter can have default value .
# -->Default arguments are used when the caller doesnot provide that argument .
# -->Ex -
# def greet(name, message="Hello"):
#     print(message, name)

# greet("Rahul")

# KEYWORD ARGUMENT :
# -->Insert the passing value according to position , we can specyfy the name .
# def student(name, age):
#     print(name)
#     print(age)
# #student("jyoti",32)#Positional argument .

# student(age=21, name="Rahul")#key word argument .


# *args :
# -->Args is use to when we dont know how many positional argument will be  .
# -->*args allwos to function to accept multiple positional argument .
# def add(*numbers):
#     total = 0

#     for num in numbers:
#         total += num

#     return total


# print(add(10, 20))
# print(add(10, 20, 30))
# print(add(10, 20, 30, 40))


# # in side thee function , number behave like tuple .
# def show(*args):
#     print(args)


# show(10, 20, 30)


# **kwaargs :

# --> It allow to function accept multiple key word argument .
# -->Inside the function details behave like dicitionary .


# def student(**details):
#     print(details)


# student(name="jyoti", age=21, city="cuttack")


# def student(**details):
#     for key, value in details.items():
#         print(key, ":", value)


# student(name="Rahul", age=21, course="Python")


# | Syntax     | Used for                      | Inside function |
# | ---------- | ----------------------------- | --------------- |
# | `*args`    | Multiple positional arguments | Tuple           |
# | `**kwargs` | Multiple keyword arguments    | Dictionary      |


# Scope :

# -->Scope defines where a variable can be accessed in a Python program.
# -->Python use  the LEGB rule find the variable .
x = 10  # Global


def test():
    x = 20  # Local
    print(x)


test()  # 20
print(x)  # 10
