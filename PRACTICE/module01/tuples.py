# TUPLES :
# -->Tuples is a collection of multiple values stored together .
# -->it has mentain order of an element .
# -->It has immmutable -it cannot be change after creation .
# -->Allows Duplicates -Same value appeair multiple times .

data = (10, 20, 30, 40, 50)
print(data)

# Access tuple element :

print(data[0])
print(data[-1])

# Immutable :
# data[0] = 100

data = (100, 200, 300)

print(data)

# tuple allow auplicate :

data = (100, 100, 20, 20, 30, 40)
print(data)

# Tuple Method :
# --> tuppls have fewer method because they cannpt modify .

# count() : count how many a value appears .


data = (10, 20, 20, 30)

print(data.count(30))
print(data.count(10))
print(data.count(20))

# index() : return the index of value .

data = (10, 20, 30)

print(data.index(20))



