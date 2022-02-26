def make_album(artist_name, album_title, number_of_songs = None):
	"""Function will make an album"""

	if number_of_songs:
		album = {'name': artist_name, 'title': album_title, 'number': number_of_songs}
		return album
	else:	
		album = {'name': artist_name, 'title': album_title}
		return album


while True:
	print('Please enter the name of an artist.')
	print("Enter 'q' at any time to quit: ")
	artist_name = input('Artist: ')
	if artist_name == 'q':
		break
	else:	
		album_title = input('Album: ')
		if album_title == 'q':
			break
		else:
			album = make_album(artist_name, album_title)
			print(album)