"""Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string"""

str1=input("enter the first string:")
str2=input("enter the second string:")

main_str1 = str2[:2] + str1[2:]
main_str2 = str1[:2] + str2[2:]

result = main_str1 + " " + main_str2

print("result:", result)

