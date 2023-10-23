
"""Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30
"""

values = [x**2 for x in range(1, 31)]

first = values[:5]

last = values[-5:]

print("First 5 elements:", first)

print("Last 5 elements:", last)
