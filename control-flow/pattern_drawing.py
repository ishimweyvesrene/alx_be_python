# control-flow/pattern_drawing.py

# Prompt user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")  # print stars side by side
    print()  # move to the next line
    row += 1
