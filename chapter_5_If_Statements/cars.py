cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print('Hold the anchovies!')

# Activity provided below. Pg. 78.

age = 21
print('Is the person old enough to drink? I predict True.')
print(age >= 21)

age = 18
print('Is the person old enough to drink? I predict False.')
print(age >= 21)


# Activity provided below. Pg. 84.

alien_color = 'green'

if alien_color == 'green':
	print('You just earned 5 points!')
elif alien_color == 'yellow':
	print('You just earned 10 points!')
else:
	print('You just earned 15 points!')

age = 65

if age < 2:
	print('You are a baby.')
elif age >= 2 and age < 4:
	print('You are a toddler.')
elif age >= 4 and age < 13:
	print('You are a kid.')
elif age >= 13 and age < 20:
	print('You are a teenager.')
elif age >= 20 and age < 65:
	print('You are an adult.')
else:
	print('You are an elder.')

favorite_fruits = ['banana', 'strawberry', 'pineapple']


if 'banana' in favorite_fruits:
	print('You really like bananas!')
if 'strawberry' in favorite_fruits:
	print('You really like strawberries!')
if 'pineapple' in favorite_fruits:
	print('You really like pineapples!')
if 'mango' in favorite_fruits:
	print('You really like mangos!')
if 'blackberry' in favorite_fruits:
	print('You really like blackberries!')

