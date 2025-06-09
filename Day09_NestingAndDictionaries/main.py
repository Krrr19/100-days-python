# Day 9: Nesting and Dictionaries

travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lyon"],
        "visits": 3
    },
    {
        "country": "Kenya",
        "cities": ["Nairobi", "Mombasa"],
        "visits": 5
    }
]

# Manually adding a new country (we'll skip functions for now)
new_country = {
    "country": "Japan",
    "cities": ["Tokyo", "Kyoto"],
    "visits": 2
}

travel_log.append(new_country)

# Show all travel logs
print("\nYour Travel Log:")
for entry in travel_log:
    print(f"\nCountry: {entry['country']}")
    print(f"Cities Visited: {', '.join(entry['cities'])}")
    print(f"Number of Visits: {entry['visits']}")
