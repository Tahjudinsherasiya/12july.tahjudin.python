
"""Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.
"""

def new_string(input_string):
    if len(input_string) < 2:
        return ""
    
    new_string = input_string[:2] + input_string[-2:]
    return new_string

user_input = input("Enter a string: ")
result = new_string(user_input)
print("New string:", result)
