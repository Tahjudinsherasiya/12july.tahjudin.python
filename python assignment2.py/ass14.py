
"""Write a Python program to count the occurrences of each word in a 
given sentence"""

sentence = input("enter a sentence: ").lower().replace(",", "").replace(".", "")
 
words = sentence.split()

word_occurrences = {}

for word in words:
    if word in word_occurrences:
        word_occurrences[word] +=1
    else:
        word_occurrences[word] =1 
        
print("word occurrences:")

for word, count in word_occurrences.items():
    print(f"{word}: {count}") 
     