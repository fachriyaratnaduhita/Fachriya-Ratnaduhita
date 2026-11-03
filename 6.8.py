pet_1 = {'kind': 'dog', 'owner': 'Alisya'}
pet_2 = {'kind': 'cat', 'owner': 'Bobi'}
pet_3 = {'kind': 'rabbit', 'owner': 'Jane'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    animal = pet['kind']
    owner = pet['owner']
    print(f"\nAnimal: {animal.title()}")
    print(f"Owner: {owner}")