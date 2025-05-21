# Day 2: Variables and Input

# Ask the user for their name and store it in a variable
name = input("What is your name? ")

# Greet the user
print("Hello, " + name + "!")

# Let's explore variable swapping
a = input("Enter value for a: ")
b = input("Enter value for b: ")

# Swap the values
a, b = b, a

print("After swapping:")
print("a = " + a)
print("b = " + b)
