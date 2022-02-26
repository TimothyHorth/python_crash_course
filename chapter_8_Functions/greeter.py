def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('tim')


def display_message():
	"""Prints one sentence telling everyone what you are learning about in this chapter"""
	print('We are learning about defining functions, parameters, and arguments.')

display_message()


def favorite_book(book):
	"""Tells which book is your favorite"""
	print(f'One of my favorite books is {book.title()}.')

favorite_book('alice in wonderland')


def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f'\nI have a {animal_type}.')
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(animal_type = 'dog', pet_name = 'willie')