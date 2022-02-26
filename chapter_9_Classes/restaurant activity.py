# class Restaurant:
# 	"""Print the name and cuisine type of a given restaurant instance."""

# 	def __init__(self, restaurant_name, cuisine_type):
# 		"""Pass the restaurant name and cuisine type."""
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		"""Method prints the name and cuisine type."""
# 		print(f"The name of the restaurant is {self.restaurant_name.title()}.")
# 		print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

# 	def open_restaurant(self):
# 		"""Method prints a message stating that the restaurant is open."""
# 		print(f'{self.restaurant_name.title()} is open!')

# my_restaurant = Restaurant('Five Guys', 'American')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# restaurant_two = Restaurant('Olive Garden', 'Italian')
# restaurant_two.describe_restaurant()

# restaurant_three = Restaurant('Panda Express', 'chinese')
# restaurant_three.describe_restaurant()

class User:
	"""Obtain first and last name."""

	def __init__(self, first_name, last_name, age, hometown):
		"""Pass first and last name arguments."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = int(age)
		self.hometown = hometown

	def describe_user(self):
		"""Print summary of user's info."""
		print(f'Name: {self.first_name.title()} {self.last_name.title()}')
		print(f'Age: {self.age}')
		print(f'Hometown: {self.hometown}')

myself = User('Timothy', 'Horth', 26, 'Akron, OH')
myself.describe_user()
