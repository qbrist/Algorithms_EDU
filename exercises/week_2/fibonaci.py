#Uses Python3
from multiprocessing import Process

def fibonaci_naive(n):
	if n <= 1:
		return n
	else:
		return fibonaci_naive(n-1) + fibonaci_naive(n-2)

def fibonaci_abitfaster(n):
	if n <= 1:
		return n
	fib = []
	fib.append(0)
	fib.append(1)
	for i in range(2,n):
		fib.append(fib[i-1]+fib[i-2])
	return fib[n-1]

def print_fib_naive(n):
	print("Fibonaci number naive ", n, "is :",fibonaci_naive(n))

def print_fib_abitfaster(n):
	print("Fibonaci number abitfaster ", n, "is :",fibonaci_abitfaster(n))


if __name__ == '__main__':
	print("Enter the number:")
	n = int(input())

	p_naive = Process(target = print_fib_naive, args = (n,))
	p_abitfaster = Process(target = print_fib_abitfaster, args = (n,))

	p_naive.start()
	p_abitfaster.start()
	p_naive.join()
	p_abitfaster.join()


	
	
