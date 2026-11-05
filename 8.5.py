def describe_city(city, country='Indonesia'):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('jakarta')
describe_city('tokyo', 'japan')
describe_city('paris', 'france')
describe_city('surabaya')