#Uses Python3

def GCD(a,b):
	if a == 0:
		return b
	if b == 0:
		return a
	if a >= b:
		return GCD(a%b,b)
	if b >= a:
		return GCD(a,b%a)

a = int(input())
b = int(input())

print(GCD(a,b))