
"""Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5"""

n1=int(input("enter the first integer:"))
n2=int(input("enter the second integer:"))

if n1 == n2:
    print("true")
else:
    sum = n1 + n2
    diff = n1 - n2
    
print(sum)