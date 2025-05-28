# Day 4: String Manipulation

# Ask the user for their name
name = input("What is your name? ")

# Print the name in different ways
print("Hello, " + name + "!")
print("Your name in uppercase is:", name.upper())
print("Your name in lowercase is:", name.lower())
print("Your name has", len(name), "characters.")

# Let's access specific characters
print("The first letter of your name is:", name[0])
print("The last letter of your name is:", name[-1])
