# exercise 8.3
def make_shirt(size, message):
    """Summarize the size and message of the shirt."""
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")

# Using positional arguments
make_shirt("Medium", "Good Mood!")

# Using keyword arguments
make_shirt(size="Large", message="Stay Healthy!")

# exercise 8.5
def describe_city(city, country='Indonesia'):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('jakarta')
describe_city('tokyo', 'japan')
describe_city('paris', 'france')
describe_city('surabaya')

# exercise 8.7
def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

album_1 = make_album('feby putri', 'hitam putih')
album_2 = make_album('blackpink', 'born pink', 8)
album_3 = make_album('niki', 'nicole')

print(album_1)
print(album_2)
print(album_3)