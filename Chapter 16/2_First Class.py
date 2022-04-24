# Objective

# Question---> What is a class ?
# Answer---> Python is an OOP language. Almost everything in python is an object, with its properties and methods . A
# Class is like an object constructor or a 'Blueprint' for creating objects.



# Question---> What is inti method ?
# Answer ---> init __init__ is one of the reserved methods in Python . In object oriented programming, it is known as a
# constructor.The __init__ method can be called when an object is created from the class, and access is required to
# initialize theattributes of the class.


# Question---> What are Attributes , Instance variables ?
# Answer ---> An instance attribute is a Python variable belonging to one, and only one, object. This variable is only
# accessible inthe scope of this object and it is defined inside the constructor function, __init__ (self,..) of the
# class


# Question---> How to create our object ?
# Answer ---> Python Object Initialization. When we create object for a class, the __init__ () method is called. We use
# this to fill... Assigning One Object to Another Python Object. Like we do with any other construct in Python, it is
# possible to assign... Assigning Attributes to an Object ...


# Question---> How to create an class ?
class Person:
    def __init__(self,first_name,Last_name,age,color):
        # instant variables
        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age
        self.color = color

p1 = Person('Uttam','Singh',20,'Brown')
p2 = Person('Ravi','Singh',20,'Brown')
print(p1.first_name)
print(p1.Last_name)


print(p2.first_name)
print(p2.Last_name)
