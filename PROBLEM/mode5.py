# Problem 5: Employee Salary Comparison
# An HR executive wants to compare the salaries of two employees.
# Write a program that accepts the salaries of both employees and determines whose salary is higher.
# If both salaries are the same, the program should indicate that they are equal.

# program to compair salery of two employee ?

salery1 = float(input("Enter the salery of Employee 1: "))
salery2 = float(input("Enter the salery of Employee 2: "))

# compair and display the results
print("\n---Salery Comaresion---")
print(f"Employee 1 Salery : {salery1}")
print(f"Employee 2 Salery : {salery2}")


if salery1 > salery2:
    print("Emplyee 1 has higher salery. ")
elif salery2 > salery1:
    print("Employee 2 has a higher salery. ")
else:
    print("Both employees has equal salaries.")

print("-----------------------------------------")
