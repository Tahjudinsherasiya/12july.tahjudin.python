
"""Write a Python program to map two lists into a dictionary
"""

t1 = ['a', 'b', 'c']
t2 = [1, 2, 3]

pairs = zip(t1, t2)

dict = dict(pairs)

print("Mapped:")
print(dict)