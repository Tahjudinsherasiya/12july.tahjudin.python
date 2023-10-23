
"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string
"""

my_string = 'tahjudin'

my_dict = {letter: my_string.count(letter) for letter in my_string}
print(my_dict)