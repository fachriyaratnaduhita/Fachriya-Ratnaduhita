favorite_places = {
    'Dina': ['japan', 'switzerland', 'iceland'],
    'Lita': ['hawaii'],
    'Zakaria': ['paris', 'rome'],
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")