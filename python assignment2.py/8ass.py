
"""Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5."""


def condition(a, b):
    if a == b or abs(a - b) == 5 or a + b == 5:
        return True
    else:
        return False

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
result = condition(num1, num2)

if result:
    print("True")
else:
    print("False")