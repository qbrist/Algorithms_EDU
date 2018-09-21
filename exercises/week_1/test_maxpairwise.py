#Uses python3
import random

def MaxPairWiseFast(numbers):
	index_1 = 0

	for i in range(0,len(numbers)):
		if numbers[index_1] <= numbers[i]:
			index_1 = i

	if index_1 == 0:
		index_2 = 1
	else:
		index_2 = 0

	for j in range(1,len(numbers)):
		if j != index_1 and numbers[index_2] <= numbers[j]:
			index_2 = j 

	#print(index_1,"=",numbers[index_1],"     ",index_2,"=",numbers[index_2])
	return numbers[index_1]*numbers[index_2]

def MaxPairWiseUltraFast(numbers):
	numbers.sort()
	numbers.reverse()
	return numbers[0]*numbers[1]


def MaxPairWiseNaive(numbers):
	product = 0

	for i in range(n):
		for j in range(i + 1, n):
			product = max(product, numbers[i] * numbers[j])

	return product

n = int(input())
m = int(input())
numbers = []
mark = 0


while(mark == 0):
	for i in range(0,n):
		numbers.append(random.randint(0,m))
	
	fast = MaxPairWiseFast(numbers)
	ultra = MaxPairWiseUltraFast(numbers)
	#naive = MaxPairWiseNaive(numbers)
	
	#print(numbers)
	
	if fast == ultra:
		print("OK fast = ",fast," ultra = ",ultra)
		numbers.clear()
	else:
		print("WRONG: fast = ",fast," ultra = ",ultra)
		mark = 1