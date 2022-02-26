from random import randint

class Die:
	"""Class that rolls a die"""

	def __init__(self, sides=6):
		"""Initialize an instance of a die"""
		self.sides = sides

	def roll_die(self):
		"""Print a random number between 1 and # of sides the die has"""
		print(f'You rolled {randint(1,self.sides)}!')

die_1 = Die(20)
for i in range(0,10):
	die_1.roll_die()
