person1 = {'first_name':'Ica', 
          'last_name':'Khairunnisa', 
          'age':18, 
          'city':'Jakarta'
}

person2 = {'first_name':'Raisya', 
          'last_name':'Aulia', 
          'age':17, 
          'city':'Sukoharjo'
}

person3 = {'first_name':'Lila', 
          'last_name':'Saraswati', 
          'age':21, 
          'city':'Surabaya'
}

people = [person1, person2, person3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"\nName: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}")