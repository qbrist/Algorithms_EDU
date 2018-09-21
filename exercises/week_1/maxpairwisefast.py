# Uses python3

n = int(input())
numbers = [int(x) for x in input().split()]

numbers.sort()
numbers.reverse()

print(numbers[0]*numbers[1])
