
"""Write a Python program to read an entire text file.
"""

def file_read(my_file):
        txt = open(my_file)
        print(txt.read())

file_read('my_file.txt')