# Day 10: Understanding Print vs Return in Functions

# Function that prints the square of a number
def print_square(number):
    print("Inside print_square():")
    print(number ** 2)

# Function that returns the square of a number
def return_square(number):
    return number ** 2

# Call the first function
print_square(5)  # Outputs: 25 but doesn't store the result

# Call the second function
result = return_square(5)
print("Returned value from return_square():", result)

# Demonstrating the difference
print("Can we store the result of print_square()? Let's try:")
x = print_square(6)
print("Result stored from print_square():", x)  # Will show None

y = return_square(6)
print("Result stored from return_square():", y)  # Will show 36
