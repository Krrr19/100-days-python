# Type Conversion
age = input("How old are you? ")
print("You will be " + str(int(age) + 1) + " next year.")

# Mathematical Operations
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / height ** 2
print("Your BMI is: " + str(round(bmi, 2)))

# Floor Division and Modulus
print("15 divided by 4 is:", 15 // 4, "with a remainder of", 15 % 4)
