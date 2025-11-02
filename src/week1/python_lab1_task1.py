"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    try:
        r = float(input("Enter the circle radius: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        if r < 0:
            print("Radius must be non-negative.")
        else:
            print(f"Area: {circle_area(r):.2f}")
