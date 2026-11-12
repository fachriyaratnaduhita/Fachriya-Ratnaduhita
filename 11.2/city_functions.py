
def get_city_country(city, country, population=''):
    """Return a string formatted like 'City, Country - population xxx'."""
    if population:
        output = f"{city.title()}, {country.title()} - population {population}"
    else:
        output = f"{city.title()}, {country.title()}"
    return output