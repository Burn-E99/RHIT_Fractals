from math import *
print("Heron formula solver")
sides = [0, 0, 0]
a = input("First side length: ")
b = input("Second side length: ")
c = input("Third side length: ")

sides[0] = float(a)
sides[1] = float(b)
sides[2] = float(c)

s = (sides[0] + sides[1] + sides[2])/2
area = (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))**.5
perim = sides[0] + sides[1] + sides[2]

print("Sides: ", sides)
print("Area: ", area)
print("Perimeter: ", perim)