# Anjelica Waller
# 9/16/2026
# P2Lab1
# A program that calculates the area of a circle.

# Import the math module to access mathematical functions
import math

# Prompt the user to enter the radius of the circle
circle_radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using the formula: area = π * radius^2

circle_diameter = circle_radius * 2
circle_circumference :.2 = 2 * math.pi * circle_radius
circle_area :.3 = math.pi * (circle_radius ** 2)

# Display calculations to the user
print("The diameter of the circle is:", (circle_diameter))
print("The circumference of the circle is:", f"{circle_circumference:.2f}")
print("The area of the circle is:", f"{circle_area:.3f}")
