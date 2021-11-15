class User:
	"""Obtain first and last name."""

	def __init__(self, first_name, last_name, age, hometown):
		"""Pass first and last name arguments."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = int(age)
		self.hometown = hometown
		self.login_attempts = 0

	def describe_user(self):
		"""Print summary of user's info."""
		print(f'Name: {self.first_name.title()} {self.last_name.title()}')
		print(f'Age: {self.age}')
		print(f'Hometown: {self.hometown}')

	def increment_login_attempts(self):
		"""Increment login attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts."""
		self.login_attempts = 0

myself = User('Timothy', 'Horth', 26, 'Akron, OH')
myself.describe_user()
myself.increment_login_attempts()
myself.increment_login_attempts()
print(myself.login_attempts)
myself.reset_login_attempts()
print(myself.login_attempts)