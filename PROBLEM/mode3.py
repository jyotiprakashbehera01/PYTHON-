# Problem 3: Designing a Garden 
# A gardener wants to know the amount of fencing and grass required for a rectangular garden. 
# Create a program that asks for the length and breadth of the garden, 
# calculates both the area and the perimeter, and displays the results. 

# program to calculate fencing and grass requared for a rectangulart garden ?

# Ask for length or breath :
length = float(input("Enter the length of the garden(in meters): "))
breadth = float(input("Enter thr breath of the garden(in meters): "))

# Calculate area and parameter:
area = length * breadth
perimeter = 2 * (length + breadth)

# Display the result :
print("\n---Garden Details---")
print(f"Length    :{length}meters")
print(f"Breadth   :{breadth}meters")
print(f"Area      :{area}square meter (grass required)")
print(f"perimeter :{perimeter}meters (fencing required)")
print("--------------------------------------------------")
