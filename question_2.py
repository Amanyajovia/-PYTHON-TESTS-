#Question_2(a)
import math
#Using a function, create a program that calculates the volume of a cylinder. V = pie*r*2h
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
pie = math.pi
volume = pie * radius**2 * height
print(f"The volume of the radius {radius} and the height {height} of the cylinder: {volume:.2f}")