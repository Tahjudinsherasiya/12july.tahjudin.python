
"""Write a Python program to find the highest 3 values in a dictionary
"""

from heapq import nlargest
 
my_dict = {'a':500,'b':5874,'c':560,'d':400,'e':5865,}
thrre_latgest= nlargest(3,my_dict,key=my_dict.get)
print(thrre_latgest)