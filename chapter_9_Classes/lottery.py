from random import choice

possible_selection = [1, 'x', 2, 'f', 3, 4, 'g', 5, 6, 7, 'l', 8, 9, 'p', 10]

my_ticket = '25f9'

winning_ticket = ''

counter = 0

while winning_ticket != my_ticket:
	counter+=1
	winning_ticket =''
	for i in range(0,4):
		selection = str(choice(possible_selection))
		winning_ticket += selection


print(f'You won! It took {counter} tries to have a winning ticket.')