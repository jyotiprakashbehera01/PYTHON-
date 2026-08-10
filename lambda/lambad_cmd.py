# Lambada argument : Expression
#small and anonymous function

# square = lambda number : number * number
# print("\n1. square of 5 :",square(5))

# add =  lambda a,b : a+b
# print(add(4,5))

# check_even_odd = lambda number : "Even" if number % 2 == 0 else "odd"
# print("\n3. is 7 even or odd ?:",check_even_odd(7))
# print(" is 10 even or odd ? :", check_even_odd(10))

print_multiple = lambda number : [(number * i) for i in  range(1,11)]
print(print_multiple(2))

