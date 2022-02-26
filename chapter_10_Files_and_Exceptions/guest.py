filename = 'guest.txt'

name = ''

with open(filename, 'a') as object_file:
	object_file.write('GUESTBOOK:\n\n')

	while name != 'q':
		name = input('What is your name?: (\'q\' to quit)   ')
		print(f'Hello, {name.title()}!')

		if name != 'q':
			object_file.write(f'{name.title()}\n')