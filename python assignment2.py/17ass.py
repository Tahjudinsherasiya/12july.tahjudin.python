
""" Write a Python function that takes a list of words and returns the length 
of the longest one.
"""


def length(list):
    max_length = 0
    for word in list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


words =["apple", "banana", "cherry", "grapefruit"]
print(length(words))

