
"""Write a Python program to get the Fibonacci series of given range.
"""


num = 10
n1, n2 = 0, 1
print("F1:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


