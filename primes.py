import math
import sys

def find_next_prime(n):
	n = int (n)
	n = n + 1
	x = math.factorial(n - 1)
	count = 0
	is_prime = 0
	while is_prime == 0:
		if (x % n) == (n -1):
			print "the next prime is "
			print n
			is_prime = 1
		else:
			print "calculating..."
			n = n + 1
			x = math.factorial(n - 1)
			count = count + 1
			if count == 100:
				print "the system has performed 100 iterations with no prime.."
				sys.exit()


find_next_prime(raw_input('enter a whole number -> ')) 
