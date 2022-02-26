Active = True

i = 0

divisor = -3
dividend = 7

while Active:
	if divisor == 0:
		break
	elif divisor > 0:
		if divisor <= dividend:
			i += 1
			dividend -= divisor
		else:
			break
	else:
		if (divisor * (-1)) <= dividend:
			i -= 1
			dividend += divisor
		else:
			break

print(i)