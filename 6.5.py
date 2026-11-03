rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(f"-{river.title()}")

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")