class Solution:
    def countPrimes(n):
        
        count = 0
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 1
        else:
            #Check each number less than n to see if it is a prime number
            for i in range (2, n):
                division_count = 0
                #Create range of numbers less than i to divide them by
                for j in range(2, i):
                    if i % j != 0:
                        division_count += 1
                    else: 
                        break
                if division_count == i-2:
                    count += 1
            return count

answer = Solution.countPrimes(10)

print(answer)