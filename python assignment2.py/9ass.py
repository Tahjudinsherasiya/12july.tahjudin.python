
""" Write a python program to sum of the first n positive integers."""



"""num = 16

if num < 0:
   print=int(input("Enter a positive number"))
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
"""

n = int(input("Enter a positive integer: "))

total = n * (n+1) / 2

print("The sum of the first",n,"positive integers",total)