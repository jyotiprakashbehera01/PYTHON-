import numpy as np

# -->list is flexible .multiple data dype .
# #-->array faster ,homogenious .
str_var = "Python"
# -->string content undr Double cotetion .
int_var = 21
# integer content hole number .
float_var = 21.1
#
bool_var = True
# It content true or false .
dict_var = {"name": "jyoti", "age": 21, "percentage": 70.2}
# It has odit collect store  item .
list_var = ["apple", 21, 20.1, True]
tuple_var = ("jyoti", 21, True, 21.3)
# It content odit value .
# Order collect of an item is called set .
# --> It mutable , that cannot add duplicate value .
set_1 = {10, 20, 30, 40, 50, 60}
print(set_1)
# add two variable ?
print(int_var, " ", str_var)
print(str_var + " " + str(int_var))
# It use concatinate .(Type conactinate)
# second approch :
print(f"{str_var} {int_var}")
# Declared array
# numpy--> is numeric python .
# array - It is a structure to store multiple valu in single variable .

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
# array is collection of value it arrange row and culum
print(dict_var.keys())
print(dict_var.values())
print(dict_var.items())
# find only age ?
print(dict_var.get("aaAA"))
# it use function , ti continew has function it provide none
print(dict_var["age"])
# it stop the program .It can't use function .
for key, value in dict_var.items():
    print(f"{key} {value}")

set_2 = {30, 40, 50, 60}
set_3 = {70, 80, 90, 10}
# unian all valu
print(set_2.union(set_3))
# intersection
print(set_2.intersection(set_3))
# difference
print(set_1.difference(set_2))
print(set_2.difference(set_1))
# system_difference
print(set_2.symmetric_difference(set_3))


# Conditional state ment :

num = int(input("Enter your number :"))
if num >= 90:
    print("EXLENT")
elif num >= 80:
    print("good")
elif num >= 60:
    print("average")
else:
    print("poor")
    
