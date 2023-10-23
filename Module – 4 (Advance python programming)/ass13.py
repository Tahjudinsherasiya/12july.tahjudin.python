
"""Write a Python program to copy the contents of a file to another file
"""
file1 = open('my_file.txt', 'r')

file2 = open('my_file.txt', 'w')

copy_data = file1.read()

file2.write(copy_data)

