
"""Write a Python program to count the occurrences of each word in a 
given sentence
"""



string=input("Enter sr:")
word=input("Enter wo:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
      print("Count of the word is:")
      print(count)


