
"""Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero.
"""


A=int(input("enter your number:"))
B=int(input("enter your number:"))
C=int(input("enter your number:"))

if A==B or B==C or C==A:
    print("your sum is ziro")
else:
    print("your sum is:",A+B+C)
    