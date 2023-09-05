
"""Write a Python program to count the number of characters (character 
frequency) in a string"""

str = input("enter a str:")
frequency = {}

for char in str:
    
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char] =1
        
for char, count in frequency.items():
    print(f"{char}: {count}")