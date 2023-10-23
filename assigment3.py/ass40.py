
"""Write a Python program to returns sum of all divisors of a number
"""

num = int(input("Enter the Number :"))
div = [1]
for i in range(2, num):
	if (num % i)==0:
		div.append(i)
print("Sum of All Divisors :",sum(div))