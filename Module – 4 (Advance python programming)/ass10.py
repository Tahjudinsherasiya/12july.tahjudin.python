
"""Write a Python program to read a file line by line store it into a variable. 
"""

def file_read(my_file):
        with open (my_file , "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('my_file.txt')
