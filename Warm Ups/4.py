from math import *

print("Fibbonacci!\n")

nIn = input("Enter the number of integers to print: ")
n = int(nIn)
count, a, b = 0, 0, 1

while (count <= n):
	print(b, end = '\n')
	a, b = b, (a + b)
	count = count + 1