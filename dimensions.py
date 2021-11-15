# Tuples are lists that cannot be changed.  The values included in the lists are constants.  Tuples are designated by their use of parentheses instead of brackets

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples are technically defined by the commas. If you want to define a tuple with 1 element, it has to have a trailing comma.

# Activity provided below. Pg. 68.

foods = ('eggs', 'sausage', 'pancakes', 'waffles', 'biscuits')
for food in foods:
	print(food.title())

foods = ('eggs', 'sausage', 'pancakes', 'bagels', 'cereal')
for food in foods:
	print(food.title())

