# LIST :
# --> A list an order of an mutable collection that can store multiple value & allows duplicate element .
# --> List is the collection of value store in single variable .
# -->It has mentains  the order of element .
# -->It has mutable(when the element can be changed) .
# -->It allows duplicate (same value apper multiple time) .

numbers = [10, 20, 30, 40, 50]

print(numbers)

# access trhe element :

print(numbers[0])
print(numbers[-1])

# modify list of the element :

numbers[0] = 100
print(numbers)
# [100, 20, 30, 40, 50]

# IMPORT LIST METHOD:

# append() : add list element in the end . add one element .

number = [10, 20, 30]

number.append(40)
print(number)

# insert() : INsert an element a specific table .

number.insert(1, 15)
print(number)

# remove() : remove a specifiv value .

number.remove(15)
print(number)

# pop() : remove the element using the index , By default it remove the last element .


number.pop()
print(number)

# sort() :short the list on the assending order .

num = [20, 30, 40, 10, 25]
num.sort()
print(num)


# reverse() : reverse the order of element .

num.reverse()
print(num)

# clear() : Remove all element .

num.clear()
print(num)

# extend() : add multiple element froms another iterable .

num = [10, 20]
num.extend([30, 40, 50])
print(num)

# List Slicing :

print(num[1:3])
# when start is include and end is exclude .

# List Allows Duplicates :

number = [10, 10, 20, 20, 20, 30, 40]
print(number)
