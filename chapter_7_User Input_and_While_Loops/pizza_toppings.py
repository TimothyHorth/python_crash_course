# Pizza Toppings

prompt = "Please enter the toppings you'd like on your pizza:\n"
prompt += "Enter 'quit' when you are finished. "

message = ""

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(f'We will add {message} to your pizza!')
	else:
		break
