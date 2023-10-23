
"""Write a Python program to convert a list of tuples into a dictionary
"""

list_tuples = [('a', 1), ('b', 2), ('c', 3)]

result = {}

for tup in list_tuples:
    key, value = tup
    result[key] = value

print(result)
