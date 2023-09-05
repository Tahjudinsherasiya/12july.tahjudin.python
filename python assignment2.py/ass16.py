"""Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string"""

x = input("enter a str:")

a= x.find('not')
b= x.find('poor')

if a!= -1 and b != -1 and b>a:
    result = x[:a] + 'good' + x[b+4:]
else:
    result = x
    
print("result:", result)

