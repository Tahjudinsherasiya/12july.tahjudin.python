
"""Write a Python program to count occurrences of a substring in a string"""

a="HELLO, hello, hello!"
b="hello"

count = sum(a[i:i+len(b)] == b
        for i in range(len(a)-len(b)+1))
print(f"the substring '{b}' occurs {count} time in the string")

        