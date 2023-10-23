
"""Write a python program to find the longest words.
"""

File = open("example.txt",'r')

words = File.read().split()

max_length = max(len(word)for word in words)

longest_word = [word for word in words if len (word)==max_length]

print(longest_word)