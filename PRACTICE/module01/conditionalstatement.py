# What is conditional statement  ?
# --> a conditional statement to make a decition  based other while they check true or false .

# Q2. What are the conditional statements in Python ?
# Answer:
# The main conditional statements are:
# if
# if-else
# if-elif-else
# Nested if

# Q3. What is the difference between if and if-else ?
# Answer:
# if executes code only when the condition is true.
# if-else provides two choices: one when the condition is true and another when it is false.

# check the age child ,teenager ,adult ?

age = int(input("Enter your age :"))

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("child")

# check the student mark gradetion ?
# -->

mark = int(input("Enter your mark :"))

if mark >=90 :
    print("A+")
elif mark >=80 :
    print("A")
elif mark >=70:
    print("B+")
elif mark >=60:
    print("B")
elif mark >= 30 :
    print("C")
else:
    print("FAIl")
    
