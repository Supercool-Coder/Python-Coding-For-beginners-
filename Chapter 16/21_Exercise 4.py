# Creating class and object in python
# Class ---> A class is a blueprint for the object.
# Object ---> An object (instance) is an instantiation of a class is defined, only the description for the objecct is
# defined. Therefore, no  memory or storage is allocated.
# Instance ---> An instance is a specific object created from a particular class.



class Dog:
    # Attributes
    species = 'Honest pet'

    def __init__(self,name,age):
        self.name = name
        self.age = age

# Instance the Dog class
dost = Dog('Tommy',5)
love = Dog('Gummy',8)

# Access the class attributes
print(f"tommy is a {dost.__class__.species}")
print(f"Gummy is also a {love.__class__.species}")

# Access the Instance attributes
print(f"{dost.name} is {dost.age} years old")
print(f"{love.name} is {love.age} years old")