from math import *
import sys

print("Prime number finder\n")

def is_prime(n):
	if n%2 == 0:
		return False
	for i in range(3, (int(sqrt(n)) + 1), 2):
		if n%i == 0:
			return False
	return True

bIn = input("Number: ")

p = 2
b = int(bIn)

print("\nList of Primes:\n")
if is_prime(b):
	print(b)
	sys.exit()
else:
	while not is_prime(b):
		# print("testing b:",b)
		test = b%p
		if test == 0:
			print(p)
			b = b / p
		else:
			# print("Not: ", p)
			p += 1
			while not is_prime(p):
				p = p + 1
	print(int(b))
	print()