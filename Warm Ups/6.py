from math import *

print("Positive Divisors\n")

nIn = input("Input Number: ")
n = int(nIn)

cDiv = 1
divisors = []

while cDiv <= n:
	test = n%cDiv
	if test == 0:
		divisors.append(cDiv)
		cDiv += 1
		continue
	else:
		cDiv += 1
		continue

print()
print(divisors)
print()