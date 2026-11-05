def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

print("Enter 'q' at any time to quit.")
while True:
    artist = input("\nEnter artist name: ")
    if artist == 'q':
        break
        
    title = input("Enter album title: ")
    if title == 'q':
        break
        
    album_info = make_album(artist, title)
    print(album_info)