def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Tracker!")

while True:
    name = input("\nEnter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"\n{name}, your BMI is {bmi} and you are categorized as: {category}")

    cont = input("\nWould you like to check another person? (yes/no): ").lower()
    if cont != "yes":
        print("Thank you for using the BMI Tracker!")
        break
