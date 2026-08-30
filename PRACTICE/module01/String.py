# STRING :
# -->A string is a sequence of charecter , enclose in quotes("" or '').
name = "python"
print(name)

# --> 1. Access Charecter : Python also access in index .

print(name[0])
print(name[-1])

# string Slicing : It use to get a part of string .
print(name[0:3])
print(name[::-1])  # nohtyP

# STRING METHOD :

# upper() : Conert string to uppercase .

text = "hello kiran"
print(text.upper())

# lower() : Convert to lower case .
print("KIRAN".lower())

# Strip() : Remove space to biginning and end .

text = "  hello kiran  "
print(text.strip())

# replace() : Replace one value with another .

text = "hii.. kiran"
print(text.replace("kiran", "mikuuuuuuuu"))

# split() : Convert string into list .

text = "mikuuuuu KB"
print(text.split())

# join() : Joins is list element into a string .

word = ["jyoti", "mikuuu"]
print(" ".join(word))

# find() : return the index of first occurrence .

text = "hello python"
print(text.find("python"))

# count()

text = "hello hello hello"
print(text.count("hello"))

# startswith() : check whether a string with a specific value .

text = "hello world"
print(text.startswith("hello"))

# endswith() : Checks whether a string ends with a specific value.

text = " hello python"
print(text.endswith("python"))

# What is a string in Python?
# --> A string is an immutable sequence of characters enclosed in single, double, or triple quotes.

# Is string mutable in Python?
# --> No. Strings are immutable, meaning their characters cannot be changed directly after creation.
