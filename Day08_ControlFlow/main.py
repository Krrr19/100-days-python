# Day 8: Control Flow

# Simple Age Checker
age = int(input("How old are you? "))

if age >= 18:
    print("You're an adult.")
elif age > 12:
    print("You're a teenager.")
else:
    print("You're a child.")

# Number Checker
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# BONUS: Leap Year & Days-in-Month Checker

# 1) Leap Year Check
year = int(input("Enter a year (e.g. 2025): "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 2) Days in Month
month = int(input("Enter a month number (1–12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    days = 29 if is_leap else 28
else:
    days = None

if days:
    print(f"Month {month} of {year} has {days} days.")
else:
    print("That month number isn’t valid!")
