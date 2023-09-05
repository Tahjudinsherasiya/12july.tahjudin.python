"""Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged"""


input_str = input("enter a str:")

if len(input_str)>=3:
    
    if input_str[-3:] =='ing':
        
        input_str += 'ly'
        
    else:
        
        input_str +='ing'
        
print("modifind str:", input_str)
