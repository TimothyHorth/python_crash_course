# Pg 191 activities

# 10-2

filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.replace('Python', 'C')
	print(line)