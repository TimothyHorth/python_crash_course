for value in range(1, 5):
	print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)
print(squares)

numbers = []
for number in range(1, 11):
	numbers.append(number**2)
print(numbers)

squares = [value**2 for value in range(1, 11)]
print(squares)


#Activity provided below. Pg. 60.

#for number in range(1, 21):
#	print(number)

#numbers = list(range(1, 1_000_001))
#for number in numbers:
#	print(number)

#numbers = list(range(1, 1_000_001))
#print(max(numbers))
#print(min(numbers))
#total = sum(numbers)
#print(total)

#odd_numbers = list(range(1, 20, 2))
#for value in odd_numbers:
#	print(value)

#threes = list(range(3, 30, 3))
#for value in threes:
#	print(value)

#cubes = []
#for value in range(1, 11):
#	cubes.append(value**3)
#	print(value**3)

#for value in range(1, 11):
#	print(value**3)

cubes = [value**3 for value in range(1, 11)]
print(cubes)