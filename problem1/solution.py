## Problem ##
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9 
# the sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

## Functions ##
def is_multiple_of(number, multiple):
	if (number % multiple) == 0:
		return True
	else:
		return False

def solution():
	sum = 0
	for x in range(0, 1000):
		if is_multiple_of(x, 3) or is_multiple_of(x, 5):
			sum += x
	return sum

def solution_lc():
	return sum([x for x in range(1000) if (is_multiple_of(x, 3) or is_multiple_of(x, 5))])

## Execution ##
def main():
	print(solution_lc())

if __name__ == '__main__':
	main()


