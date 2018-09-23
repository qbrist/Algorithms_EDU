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

n = input().split()

print(GCD(int(n[0]),int(n[1])))