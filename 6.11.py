cities = {
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'It is one of the most populous metropolitan areas in the world.',
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the City of Light and home of the Eiffel Tower.',
    },
    'cairo': {
        'country': 'egypt',
        'population': '10 million',
        'fact': 'Famous for its proximity to the Giza Pyramids.',
    },
}

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    print(f"\nCity: {city.title()}")
    print(f"Country: {country}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")