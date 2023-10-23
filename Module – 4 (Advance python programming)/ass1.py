
"""Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle
"""
class rectangle:
    def __init__(self):
        self.length = float(input("Enter Rectangle Length : "))
        self.width = float(input("Enter Rectangle Width : "))

    def compute_area(self):
        area = self.length * self.width
        print("Area of Rectangle is:" %area)


rectangle = rectangle()
rectangle.compute_area()
