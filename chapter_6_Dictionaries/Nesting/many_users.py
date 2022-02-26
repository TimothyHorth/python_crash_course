users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},

	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},

}

for username, user_info in users.items():
	print(f"Username: {username}")
	print(f"\tFull Name: {user_info['first'].title()} {user_info['last'].title()}")
	print(f"\tLocation: {user_info['location'].title()}\n")


# Activities on Page 112.

person_1 = {
	'first': 'Tim',
	'last': 'Horth',
	'city': 'Akron',
}

person_2 = {
	'first': 'Joe',
	'last': 'Horth',
	'city': 'Loveland'
}

person_3 = {
	'first': 'Matt',
	'last': 'Horth',
	'city': 'Amherst',
}

persons = [person_1, person_2, person_3]

for person in persons:
	print(f"{person['first'].title()} {person['last'].title()} lives in {person['city'].title()}.")


pet_1 = {
	'type': 'dog',
	'owner': 'Tim Horth',
}

pet_2 = {
	'type': 'cat',
	'owner': 'Joe Smith',
}

pet_3 = {
	'type': 'lizard',
	'owner': 'Kayla Sweder',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
	print(f"{pet['owner'].title()} owns a {pet['type']}.")


favorite_places = {
	'tim': ['greece'],
	'britt': ['italy', 'greece'],
	'jasmine': ['washington', 'memphis', 'hampton'],
}

for key, value in favorite_places.items():
	if len(value) > 1:
		print(f"{key.title()}'s favorite places are:\n")
		for place in value:
			print(f'{place.title()}')
		print('\n')	
	else:
		for place in value:
			print(f"{key.title()}'s favorite place is:\n")
			print(f'{place.title()}\n')


favorite_numbers = {
	'Tim': [18, 69, 420],
	'JoJo': [30, 40, 50],
	'Cupid': [ 21, 90],
}

for key, value in favorite_numbers.items():
	print(f"{key.title()}'s favorite numbers are: \n")
	for number in value:
		print(f'{number}')
	print('\n')


cities = {
	'norfolk': {
		'state': 'virginia',
		'population': 246_987,
		'attribute': 'military',
		},
	'clemson': {
		'state': 'south carolina',
		'population': 98_452,
		'attribute': 'college',
		},
	'atlanta': {
		'state': 'georgia',
		'population': 23_987_456,
		'attribute': 'corporate',
		},
	}

for key, value in cities.items():
	print(f"{key.title()} is in {value['state'].title()}, has a population of {value['population']}, and is a {value['attribute']} town.")



