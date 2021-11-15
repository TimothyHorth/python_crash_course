roman_numeral = 'MCMXCIV'
rn_list = list(roman_numeral)
total = 0
left = 0
right = 0

for i in range(len(rn_list)-1):
	if rn_list[i] == 'I':
		left = 1
	if rn_list[i] == 'V':
		left = 5
	if rn_list[i] == 'X':
		left = 10
	if rn_list[i] == 'L':
		left = 50
	if rn_list[i] == 'C':
		left = 100
	if rn_list[i] == 'D':
		left = 500
	if rn_list[i] == 'M':
		left = 1000

	if rn_list[i+1] == 'I':
		right = 1
	if rn_list[i+1] == 'V':
		right = 5
	if rn_list[i+1] == 'X':
		right = 10
	if rn_list[i+1] == 'L':
		right = 50
	if rn_list[i+1] == 'C':
		right = 100
	if rn_list[i+1] == 'D':
		right = 500
	if rn_list[i+1] == 'M':
		right = 1000

	if left < right:
		total -= left
	if left >= right:
		total += left

if rn_list[-1] == 'I':
	total += 1
if rn_list[-1] == 'V':
	total += 5
if rn_list[-1] == 'X':
	total += 10
if rn_list[-1] == 'L':
	total += 50
if rn_list[-1] == 'C':
	total += 100
if rn_list[-1] == 'D':
	total += 500
if rn_list[-1] == 'M':
	total += 1000

print(total)

# if 'IV' in roman_numeral:
# 	total += 4
# if 'IX' in roman_numeral:
# 	total += 9
# if 'XL' in roman_numeral:
# 	total += 40
# if 'XC' in roman_numerals:
# 	total += 90
# if 'CD' in roman_numerals:
# 	total += 400
# if 'CM' in roman numerals:
# 	total += 900