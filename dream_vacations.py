# 7-10: Dream Vacation activity

vacations = {}

prompt = 'If you could visit once place in the world, where would you go?: '

active = True

while active:
	name = input('What is your name?: ')
	destination = input(prompt)
	vacations[name] = destination
	flag = input('Do you have another dream vacation? (yes/no): ')

	if flag == 'no':
		active = False

print('\n---Poll Results---\n')
for name, destination in vacations.items():
	print(f"{name.title()} wants to go to {destination.title()}")