
"""How to Define a Class in Python? What Is Self? Give An Example Of 
A Python Class 
"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("tahjudin", 10)
p1.myfunc()