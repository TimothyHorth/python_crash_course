class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age 

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f'{self.name.title()} is now sitting.')

	def rollover(self):
		"""Simulate a dog rolling over in response to a command."""
		print(f'{self.name.title()} rolled over!')

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.rollover()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.rollover()

