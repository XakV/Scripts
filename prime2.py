##   Assignment ###
#
# Your assignment is to implement the
# following function: `find_next_prime`.
# As the name states, given the number `n` the
# function should return the next closest prime.
#
# Examples:
# * `find_next_prime(6)` should return 7.
# * `find_next_prime(10)` should return 11.
# * `find_next_prime(11)` should return 13.
#
# You can use whatever you want (data structures,
# language features, etc).
#
# Unit tests would be a plus. Actually, just knowing what
# they are would be a plus :)
#
### End Assignment ###
n = (raw_input('Enter a Number'))

def find_next_prime(n):
	is_prime = False
	print n
	x = n + 1
	print x
	while is_prime != True:
		if x%2 == 0:
			x = x + 1
			return False
		elif x%3 == 0:
			x = x + 1
			return False
		elif x%5 == 0:
			x = x + 1
			return False
		elif x%7 == 0:
			x = x + 1
			return False
		elif x%11 == 0:
			return False
			x = x + 1
		elif x%13 == 0:
			return False
			x = x + 1
		else:
			return True
			print x
	
	

pass 
