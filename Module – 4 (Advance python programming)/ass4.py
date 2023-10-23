
"""Write python program that user to enter only odd numbers, else will 
raise an exception.
"""        
try:
       a = int(input("Enter numerator number: "))
       b = int(input("Enter denominator number: "))
       print("Result of Division: " + str(a/b))
except(ValueError, ZeroDivisionError):
    print("Please check the input value: It should be an integer greater than 0")