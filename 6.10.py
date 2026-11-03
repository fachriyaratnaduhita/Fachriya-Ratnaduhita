favorite_numbers = {'Tina': [2, 5],
                    'Ani': [5, 0],
                    'Santi': [10,4],
                    'Nita': [7, 3, 4],
                    'Boni': [0, 6, 12]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")