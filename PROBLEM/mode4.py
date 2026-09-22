# Problem 4: Semester Result
# A teacher wants a quick program to calculate a student's performance.
# Ask the user to enter marks obtained in three subjects.
# The program should calculate the total marks and the average marks and display them clearly.

# program to calculate student's performance

# ask for mark into the subjects
subject1 = float(input("Enter mark obtained in subject 1: "))
subject2 = float(input("Enter mark obtained in subject 2: "))
subject3 = float(input("Enter mark obtained in subject 3: "))
subject4 = float(input("Enter mark obtained in subject 4: "))
subject5 = float(input("Enter mark obtained in subject 5: "))
subject6 = float(input("Enter mark obtained in subject 6: "))

# calculate the total and average
total = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
average = total / 3

# Display the results
print("\n---Student Porformance---")
print(f"Mark in subject1 : {subject1}")
print(f"Mark in subject2 : {subject2}")
print(f"Mark in subject3 : {subject3}")
print(f"Mark in subject4 : {subject4}")
print(f"Mark in subject5 : {subject5}")
print(f"Mark in subject6 : {subject6}")
print(f"Total Mark       : {total}")
print(f"Average Mark     : {average:.2f}")
print("--------------------------------")
