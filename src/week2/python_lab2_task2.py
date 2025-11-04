# file: lab_3_2_comprehensions_minimal.py
import random

# Fill in your own numbers or generate 10 random integers
numbers = []  # e.g., [3, 8, -2, 7, 0, -5, 10]

# Keep script runnable if left empty
if not numbers:
    numbers = [random.randint(-10, 10) for _ in range(10)]

# Comprehensions
squares = [n * n for n in numbers]
positives = [n for n in numbers if n > 0]
even_squares = {n * n for n in numbers if n % 2 == 0}
cubes = {n: n ** 3 for n in numbers}

# Output
print("Numbers:", numbers)  # why: shows the generated list when using randomness
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
