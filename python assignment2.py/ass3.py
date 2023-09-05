
"""Write a Python program to get the Fibonacci series of given range"""

start=int(input("enter the starting number:"))

a= 0
b= 1

while b <=start:
    c=a+b
    a=b
    if c <= start:
        print(c)
    a=b
    b=c
    
    