# Loop:
# --> It used to repet bloock of code in multiple iteam .
# -->in python content has .

# 1.for loop = When yor repet somthing else for Sequences, and know her raange

# 2.while loop = When you want to repet somthing when the condition is true .

# FOR LOOP:

# for i in range(5):
#     print("Hello world")

# for i in range(1, 6):
#     print(i)

# python auto detect inx value .

# for i in range(6):
#     print(i)

# check even value ?

# for i in range(0, 11, 2):
#     print(i)

# for i in range(1, 12, 2):
#     print(i)

# fruits = ["apple", "banana", "mango", "pinaapple"]
# for fruit in fruits:
#     print(fruit)

# name = "jyoti&mikii"
# for latter in name:
#     print(latter)


# # calculate sum number :

# total = 0
# for i in range(1, 6):
#     total = total + i
#     print(total)


# WHILE LOOP:


# i = 1
# while i <= 5:
#     print(i)
#     i = i+1


# # countdown:
# i = 5

# while i >= 1:
#     print(i)
#     i = i - 1

# Print multiplication table :

# num = int(input("Enter your number :"))
# for i in range(1, 11):
#     print(num*i)


# LOOP IF CONDITION:

# find the even number ?

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in number:
#     if num %2 == 0:
#       print(num)

# Check the number :

# numbers = [2, 7, 4, 9, 3, 10]

# for num in numbers:
#     if num > 5:
#         print(num)


# break in LOOP:

# -->break is used to stop the loop completely.


# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)


# # continew in looop :

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# Q.1 check the number is even or odd ?

for i in range(1, 10):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is odd")


# for	--> Repeat for each item/range
# while	-->Repeat while condition is true
# break	-->Stop the loop
# continue	-->Skip current iteration
# range()	-->Generate a sequence of numbers .
