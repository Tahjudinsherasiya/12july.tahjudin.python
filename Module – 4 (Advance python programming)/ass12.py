
"""Write a Python program to count the frequency of words in a file.
"""
file = open('my_file.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))