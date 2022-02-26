my_foods = ['pizza', 'falafel', 'carrot cake']

friends_food = my_foods[:]

my_foods.append('cannoli')
friends_food.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

# Activity provided below. Pg. 65.

sports = ['soccer', 'football', 'basketball', 'baseball', 'hockey']
print('The first three items in the list are:')
print(sports[:3])
print('Three items from the middle of the list are:')
print(sports[1:4])
print('The last three items in the lsit are:')
print(sports[-3:])

pizzas = ['pepperoni', 'cheese', 'chicken bacon ranch']
friend_pizzas = pizzas[:]
pizzas.append('meat lovers')
friend_pizzas.append('veggies lover')
print('My favorite pizzas are:')
print(pizzas)
print("My friend's favorite pizzas are:")
print(friend_pizzas)

for pizza in pizzas:
	print(pizza.title())

for pizza in friend_pizzas:
	print(pizza.title())