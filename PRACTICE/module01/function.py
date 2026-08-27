# FUNCTION :

# -->It is a reuseable block of code that perform a specific task .
# -->It can write it once inside a function and call it whenever we need it.
# -->def → keyword used to create a function
# function_name → name of the function
# () → parameters go inside these parentheses
# : → starts the function body .


def add(a, b):
    return a + b


result = add(10, 20)
print(result)

# 1.PARAMETER :
# -->parameter are the variable writen inside the function defination ,
# -->It is a place holder that receives a value .
# --> upper a , b are the parameter .

# 2.ARGUMENT :
# -->Argument is the actual value that passed when calling the function .
# -->In upper 10 ,20 are the argument .


# 3.RETURN :
# -->Return send a value back from function .
def Square(num):
    return num * num


result = Square(5)
print(result)


# RETURN vs PRINT
# ->PRINT = it has disply the result but not return .
# ->RETURN = it has give the result back so we can store or used it .


# 4.DEFULT ARGUMENT :
# -->A parameter can have default value .
# -->Default arguments are used when the caller doesnot provide that argument .
# -->Ex -
def greet(name, message="hello"):
    print(message, name)
    greet("jyoti")


 