class Restaurant:
	"""Class for a restauarant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Creates an instance of a restaurant and saves the name and cuisine type."""
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		"""Method to describe the restaurant"""
		print(f'{self.name} serves {self.type} type cuisine.')

	def open_restaurant(self):
		"""Method that prints that the restaurant is open"""
		print(f'{self.name} is open!')


restaurant = Restaurant('Two Urban Licks', 'American')
print(f'The name of the restaurant is {restaurant.name}.')
print(f'The cuisine type is {restaurant.type}.')

restaurant.describe_restaurant()
restaurant.open_restaurant()