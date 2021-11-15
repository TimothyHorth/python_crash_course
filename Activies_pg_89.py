usernames = []

if usernames:
	for username in usernames:
		if username != 'admin':
			print(f'Hello, {username.title()}! Thanks for logging in!')
		else:
			print('Hello admin, would you like to see a status report?')
else: 
	print('We need to find some users!')


current_users = ['Thorth', 'Broski', 'timtation', 'tjhorth18', 'TIMHORTH']

new_users = ['jimmy', 'tjhorth18', 'bobby', 'BROSKI', 'leon']

# Defining copy of current users list

copy_current_users = []

# Adding lower case elements of current_users to copy_current_users

for current_user in current_users:
	copy_current_users.append(current_user.lower())

for new_user in new_users:
	if new_user.lower() in copy_current_users:
		print('Sorry, that username is already taken! Please type in a new username.')
	else:
		print('That username is available!')

print(copy_current_users)


# Ordinal Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers_clean = list(range(1, 10))

for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(f'{number}th')
