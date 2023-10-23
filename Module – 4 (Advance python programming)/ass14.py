
"""Write a Python program to count the number of lines in a text file
"""

file = open('my_file.txt','r')

words = file.read().split()
count = 0

for word in words:
    count += 1
    
print(f"total no. of words : {count}")

