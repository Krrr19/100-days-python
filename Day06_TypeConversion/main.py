# --- Day 6: Type Conversion and Math ---

# Basic type conversion
age = input("How old are you? ")
print("You are " + age + " years old.")
print("You will be " + str(int(age) + 1) + " next year.")


# Converting string to integer
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum_result = int(num1) + int(num2)
print("The sum is:", sum_result)

# Converting float to int
height = float(input("What is your height in meters? "))
print("Height as integer (meters):", int(height))
weight = int(input("What is your weight in kilograms? "))

# Calculate BMI
bmi = weight / height ** 2
print("Your BMI is: ", str(round(bmi, 2)))


# --- Exercise: Tip Calculator ---

print("\n--- Tip Calculator ---")

# Ask for the total bill
bill = input("What was the total bill? $")

# Ask for the tip percentage
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

# Ask how many people are splitting the bill
people = input("How many people to split the bill? ")

# Convert inputs to float or int as needed
bill_float = float(bill)
tip_percent = int(tip)
people_count = int(people)

# Calculate total tip
tip_amount = (tip_percent / 100) * bill_float

# Add tip to bill
total_bill = bill_float + tip_amount

# Calculate per person share
per_person = total_bill / people_count

# Round to 2 decimal places
final_amount = round(per_person, 2)

# Display the result
print(f"Each person should pay: ${final_amount}")
