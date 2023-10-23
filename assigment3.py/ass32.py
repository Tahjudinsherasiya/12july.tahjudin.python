
"""Write a Python function to calculate the factorial of a number (a 
nonnegative integer) 
"""

num = int(input("enter your namber:"))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print (fact)