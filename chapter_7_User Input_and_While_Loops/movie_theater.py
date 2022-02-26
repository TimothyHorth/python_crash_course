# Movie Theater

prompt = "Please enter your age: "
prompt += "Enter 'quit' when you are finished. "



active = True

while active:
	age = input(prompt)
	if age != 'quit':
		age = int(age)
		if age <3:
			print('Your ticket is free!')
		elif age >= 3 and age < 12:
			print('Your ticket costs $12.')
		elif age >= 12:
			print('Your ticket costs $15.')
	else:
		active = False
