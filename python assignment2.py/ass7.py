
"""Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero"""

a=int(input("enter your number 1:"))
b=int(input("enter your number 2:"))
c=int(input("enter your number 3:"))

if a == b or b == c or c == a:
    print("your sum is ziro")
else:
    print("your sum is:", a+b+c)
    