
"""Write a Python function that takes a list and returns a new list with unique 
elements of the first list 
"""

def elements(input_list):

    set = set(input_list)
    list = list(set)
    return
my_list = [1, 2, 2, 3, 4, 4, 5]

result = elements(my_list)

print("List with elements:", result)