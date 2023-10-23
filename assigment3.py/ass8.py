
"""Write a Python program to convert a tuple to a string
"""

def string(input_tuple):
    
    result_string = ''.join(input_tuple)
    return result_string

my_tuple = ('H', 'e', 'l', 'l', 'o')

result = string(my_tuple)

print("Resulting string:", result)
