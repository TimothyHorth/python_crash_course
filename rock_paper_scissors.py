import random

your_move = ''
wins, losses, ties = 0, 0, 0
options = ['rock','paper','scissors']
print('ROCK, PAPER, SCISSORS')

while your_move != 'q':
	print(f'{wins} Wins, {losses} Losses, {ties} Ties')
	your_move = input('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit\n')
	if your_move == 'r':
		your_move_extended = 'rock'
	elif your_move == 'p':
		your_move_extended = 'paper'
	elif your_move == 's':
		your_move_extended = 'scissors'
	elif your_move == 'q':
		break
	else:
		print('\nThat is an invalid move!')
		continue

	computer_move = random.choice(options)
	print(f'\n{your_move_extended.upper()} versus...\n{computer_move.upper()}')

	if your_move_extended.upper() == computer_move.upper():
		print('\nIt is a tie!')
		ties += 1
	elif your_move_extended.upper() == 'ROCK':
		if computer_move.upper() == 'PAPER':
			print('\nYou lose.')
			losses += 1
		else:
			print('\nYou win!')
			wins += 1
	elif your_move_extended.upper() == 'PAPER':
		if computer_move.upper() == 'ROCK':
			print('\nYou win!')
			wins += 1
		else:
			print('\nYou lose.')
			losses += 1
	elif your_move_extended.upper() == 'SCISSORS':
		if computer_move.upper() == 'ROCK':
			print('\nYou lose.')
			losses += 1
		else:
			print('\nYou win!')
			wins += 1