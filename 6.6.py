favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll_people = ['jen', 'sarah', 'phil', 'michael', 'david', 'edward']

for person in poll_people:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"Please take our poll, {person.title()}!")