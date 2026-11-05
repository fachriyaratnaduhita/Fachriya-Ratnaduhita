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