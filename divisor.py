Active = True
i = 0
sum = 0
divisor = -3
dividend = 7

while Active:
	if divisor == 0:
		break
	if divisor > 0:
		sum += divisor
		if sum <= dividend:
			i += 1
		if sum > dividend:
			break
	if divisor < 0:
		sum -= divisor
		if sum <= dividend:
			i -= 1
		if sum > dividend:
			break

print(i)