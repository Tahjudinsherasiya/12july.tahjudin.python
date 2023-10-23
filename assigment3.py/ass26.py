
"""Write a Python program to replace last value of tuples in a lis
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "kiwi"
x = tuple(y)

print(x)

