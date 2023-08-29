
"""Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
"""

print("Enter the First String: ")
string1 = input()
print("Enter the Second String: ")
string2 = input()

print("\nString before swap:")
print("string1 =", string1)
print("string2 =", string2)

temp = string1
string1 = string2
string2 = temp

print("\nString after swap:")
print("string1 =", string1)
print("string2 =", string2)



