print("Hello Python")

# add two number

a = 10
b = 20

sum = a + b
print("sum :", sum)


# Find square of number ?

x = 5
Square = x * x
print("Square :", Square)

# find the area of circle ?

r = 5
Area = 3.14139 * r * r
print("Arae =", Area)  # 78.53

# Convert Celsius to Fahrenheit ?

c = 25

Fahrenheit = (c * 9 / 5) + 32

print("Fahenheit :", Fahrenheit)  # 77.0

# check even or odd ?

num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# check +ve or -ve ?

num = -21

if num > 0:
    print("Posetive")
elif num < 0:
    print("Negative")
else:
    print("zero")

# Find largest of two numbers ?

a = 23
b = 21

if a > b:
    print("Largest :", a)
else:
    print("Largest :", b)

# Find largest of three numbers ?

a = 10
b = 20
c = 10

if a > b and a > c:
    print("largest :", a)
elif b > a and b > c:
    print("largest :", b)
else:
    print("largest :", c)

# Check whether a number is divisible by 5 ?

num = 25

if num % 5 == 0:
    print("devisible by 5 ")
else:
    print("Not Devisible by 5 ")

# Calculate simple interest ?

p = 100
r = 5
t = 2

SI = p * t * r / 100
print("SI :", SI)

# Swap two numbers ?

a = 12
b = 13

a, b = b, a
print(a, b)

# Reverse a number ?

num = 898765

reversed = str(num)[::-1]
print(reversed)

# second approch

num = 258690

reversed = 0
while num > 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num = num // 10
    print("reversed :", reversed)

# Check palindrome number ?

num = 121

original = num
reversed = 0
while num > 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num = num // 10
    print("reversed :", reversed)

if original == reversed:
    print("It is palindrome")
else:
    print("It's not palendrome")


# Find sum of digits ?
num = 1234

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)
