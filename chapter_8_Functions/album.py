def make_album(artist_name, album_title, number_of_songs = None):
	"""Function will make an album"""
	if number_of_songs:
		album = {'name': artist_name, 'title': album_title, 'number': number_of_songs}
		return album
	else:	
		album = {'name': artist_name, 'title': album_title}
		return album


album = make_album('shinedown', 'MONSTERS', 12)
print(album)