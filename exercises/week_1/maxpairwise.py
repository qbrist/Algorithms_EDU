# Uses python3

n = int(input())
numbers = [int(x) for x in input().split()]

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
		
print(numbers[index_1]*numbers[index_2])