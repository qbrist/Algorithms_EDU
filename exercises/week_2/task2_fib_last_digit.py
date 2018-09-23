#Uses Python3
def fibonaci(n):
	if n <= 1:
		return n
	fib = []
	fib.append(0)
	fib.append(1)
	for i in range(2,n+1):
		fib.append((fib[i-1]+fib[i-2])%10)
	return fib[-1]%10


if __name__ == '__main__':
	n = int(input())

	print(fibonaci(n))