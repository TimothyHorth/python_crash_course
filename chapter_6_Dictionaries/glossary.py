# Glossary



rivers = {
	'nile': 'egypt',
	'tigris': 'turkey',
	'euphrates': 'syria',
}

for key, value in rivers.items():
	print(f"The {key.title()} river runs through {value.title()}.")

for key in rivers.keys():
	print(key.title())

for value in rivers.values():
	print(value.title())