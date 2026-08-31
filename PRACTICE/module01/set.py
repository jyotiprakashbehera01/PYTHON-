# SET :
# --> A ste is the collection use to store unique values .
# --> it doesnot allows duplicate .
# --> it has mutable .(you can add or remove the value)\
# --> It use full for fast member ship checking .


number = {1, 3, 2, 5, 6}

print(number)

# add an element :

number.add(7)
print(number)

# REMOVE AN ELEMENT :

number.remove(7)
print(number)

# discrad():Remove an element if it exists .
number.discard(9)

print(number)

# remove() gives an error when the value is not found,
#  while discard() does not.

# Union :

a = {1, 2, 3}
b = {3, 4, 5}

# print(a.union(b))

print(a | b)

# intersection ;

# print(a.intersection(b))

print(a & b)


# difference :
# -->Difference element that exist the first set but not in the secod .
a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b))

print(b.difference(a))


students_python = {"Ram", "John", "Sam"}
students_java = {"John", "Sam", "Raj"}

# Students in either course
print(students_python.union(students_java))

# Students in both courses
print(students_python.intersection(students_java))

# Students only in Python
print(students_python.difference(students_java))
print(students_java.difference(students_python))
