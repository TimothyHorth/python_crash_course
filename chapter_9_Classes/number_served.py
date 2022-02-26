class Restaurant:
	"""Print the name and cuisine type of a given restaurant instance."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Pass the restaurant name and cuisine type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Method prints the name and cuisine type."""
		print(f"The name of the restaurant is {self.restaurant_name.title()}.")
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

	def open_restaurant(self):
		"""Method prints a message stating that the restaurant is open."""
		print(f'{self.restaurant_name.title()} is open!')

	def set_number_served(self, served):
		"""Set the number of people that have been served."""
		self.number_served = served

	def increment_served(self, more_served):
		"""Increment the number of people served."""
		self.number_served += more_served

restaurant = Restaurant("Jack Brown's", 'burgers')
print(f'{restaurant.restaurant_name} has served {restaurant.cuisine_type} to {restaurant.number_served} people today.')

restaurant.number_served = 136
print(f'{restaurant.restaurant_name} has served {restaurant.cuisine_type} to {restaurant.number_served} people today.')

restaurant.set_number_served(150)
print(f'{restaurant.restaurant_name} has served {restaurant.cuisine_type} to {restaurant.number_served} people today.')

restaurant.increment_served(25)
print(f'{restaurant.restaurant_name} has served {restaurant.cuisine_type} to {restaurant.number_served} people today.')

