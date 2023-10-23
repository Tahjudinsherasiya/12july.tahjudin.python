
"""Write a Python program to read last n lines of a file
"""

with open("my_file.txt", "r") as file:            
    lines=file.readlines()
print(lines[-1])

