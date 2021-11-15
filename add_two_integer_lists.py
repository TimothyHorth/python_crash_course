def Solution(l1, l2):

	length1=len(l1)
	length2=len(l2)

	if length1 <= length2:
		for i in range(length1):
			total = l1[i] + l2[i]
			if total >= 10:
				if i+1 == len(l2):
					l2[i] = l2[i] + l1[i] -10
					l2.append(1)
				else:
					l2[i] = l2[i] + l1[i] - 10
					l2[i+1] = l2[i+1] + 1
					for p in range(i+1, length2):
						if l2[p] == 10:
							l2[p] = 0
							if p < length2-1:
								l2[p+1] += 1
							else: 
								l2.append(1)

			else:
				l2[i] = l1[i] + l2[i]
		return l2


	if length1 > length2:
		for i in range(length2):
			total = l1[i] + l2[i]
			if total >= 10:
				if i+1 == len(l1):
					l1[i] = l2[i] + l1[i] -10
					l1.append(1)
				elif l1[i+1] != 9:
					l1[i] = l2[i] + l1[i] -10
					l1[i+1] = l1[i+1] + 1
				else: 
					l1[i] = l2[i] + l1[i] - 10
					l1[i+1] = l1[i+1] + 1
					for p in range(i+1, length1):
						if l1[p] == 10:
							l1[p] = 0
							if p < length1-1:
								l1[p+1] += 1
							else: 
								l1.append(1)
			else:
				l1[i] = l1[i] + l2[i]
		return l1

l1 = [9,9,9,9,9,9,9]
l2 = []

answer = Solution(l1,l2)
print(answer)