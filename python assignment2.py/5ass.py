
""" Write a Python program to find whether a given number is even or odd, 
print out an appropriate message to the user.
"""


number = int(input("Enter a number: "))
if (number % 2) == 0:
   print("{0}is Even".format(number))
else:
   print("{0}is Odd".format(number))
