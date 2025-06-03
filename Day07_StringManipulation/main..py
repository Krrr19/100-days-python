# Day 7: String Manipulation

# Ask user for full name
full_name = input("Enter your full name: ")

# Display manipulations
print("UPPERCASE:", full_name.upper())
print("Title Case:", full_name.title())
print("Reversed Name:", full_name[::-1])

# Ask for favorite quote
quote = input("Enter your favorite quote: ")

# Remove extra spaces
quote = quote.strip()

# Display quote info
print("Quote Length:", len(quote), "characters")
print(f"Your favorite quote is: '{quote}'")

#  Display initials
initials = "".join([name[0].upper() for name in full_name.split()])
print("Your initials are:", initials)

# Count how many words are in the quote
word_count = len(quote.split())
print("Your quote has", word_count, "words.")



