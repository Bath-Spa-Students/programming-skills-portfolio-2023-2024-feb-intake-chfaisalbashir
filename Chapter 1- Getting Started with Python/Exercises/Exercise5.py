
 # Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

# enter the radius
radius = float(input("Enter the radius of circle: "))

# Calculate the area of the circle.
area = math.pi * radius ** 2

# print the area of the circle
print(f"The circle of area with radius is  {radius} units is: {area:.2f} square units")
