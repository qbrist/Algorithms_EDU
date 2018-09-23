#Uses Python3
def fibonaci(n,m):
	if n <= 1:
		return n
	fib = []
	fib.append(0)
	fib.append(1)
	for i in range(2,n+2):
		fib.append((fib[i-1]+fib[i-2])%m)
	print(fib)
	return fib[-1]%m


if __name__ == '__main__':
	n,m = map(int, input().split())

	delta = n%m
	print(delta)
	print(fibonaci(delta,m))