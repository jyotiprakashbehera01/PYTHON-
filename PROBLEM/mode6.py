# Problem 6: Temperature Analysis
# A weather station records temperatures throughout the day.
# Write a program that accepts a temperature value and determines whether it is above zero, below zero, or exactly zero.

# program to check temprature status :

# ask for temprature value
temperature = float(input("Enter the temperature value (in C): "))

print("\n---Temprature Status---")
if temperature > 0:
    print("The Temperature is above zero. ")
elif temperature < 0:
    print("The Temperature is below zero. ")
else:
    print("The Temperature is exactly zero. ")
print("---------------------------------------")
