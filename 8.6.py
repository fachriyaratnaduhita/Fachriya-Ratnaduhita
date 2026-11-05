def city_country(city, country):
    """Return a formatted string of city and country."""
    return f"{city.title()}, {country.title()}"

place_1 = city_country('yogyakarta', 'indonesia')
place_2 = city_country('tokyo', 'japan')
place_3 = city_country('kucing', 'malaysia')

print(place_1)
print(place_2)
print(place_3)