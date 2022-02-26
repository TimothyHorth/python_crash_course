filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()


continuous_string =''
for line in lines:
	continuous_string += line.strip()

birthday = input('Enter your birthday (mmddyy): ')

if birthday in continuous_string:
	print('Your birthday appears in pi!')
else:
	print('Your birthday does NOT appear in pi.')