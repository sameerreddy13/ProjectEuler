## Functions ##

# Recursive 
def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n - 2) + fib(n - 1)

# Using generator
def fib_gen(n):
	fib_one = 0
	fib_two = 1

	for _ in range(0, n):
		yield fib_one
		fib_one, fib_two = fib_two, fib_one + fib_two

# Iterative 
def fib_iter(n):
	fib_one = 0
	fib_two = 1

	if n == 0 or n == 1:	
		return n
	else:
		for i in range(0, n):
			fib_one, fib_two = fib_two, fib_one + fib_two

	return fib_one

## Execution ##
def main():
	print_n = 10
	index = 0

	print("Generator fib:")
	print("n ", "fib")
	for fib_result in fib_gen(print_n):
		print(index," ", fib_result)
		index += 1

	print()

	print("Recursive fib:")
	print("n ", "fib")
	for i in range(0, print_n):
		print(i, " ", fib(i))

	print()

	print("Iterative fib:")
	print("n ", "fib")
	for i in range(0, print_n):
		print(i, " ", fib_iter(i))

if __name__ == '__main__':
	main()

