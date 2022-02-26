filename = 'programming_poll.txt'

with open(filename, 'a') as object_file:

	object_file.write('WHY PEOPLE LIKE PROGRAMMING:\n\n')

	reason = ''

	while reason != 'q':
		reason = input('Why do you like programming? (\'q\' to quit)   ')
		if reason != 'q':
			object_file.write(f'{reason}\n')