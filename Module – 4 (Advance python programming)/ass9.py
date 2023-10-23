
"""Write a Python program to read a file line by line and store it into a list
"""

with open('my_file.txt') as f:
    content = f.readlines(1)
li = [x.strip() for x in content]
print(li)
