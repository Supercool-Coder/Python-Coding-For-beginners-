# Raise error example 1
# Not Implemented Error
# Abstract method ---> iska mtlb humko function mein kuch define nhi krna hai bs NotImplemented error ko raise krna hai

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplemented('You have to define this method in subclasses')

class Dog(Animal):
    def __init__(self,name,breed):
        super(Dog, self).__init__(name)
        self.breed = breed

    def sound(self):
        return 'Bhao Bhao'

class Cat(Animal):
    def __init__(self,name,breed):
        super(Cat, self).__init__(name)
        self.breed = breed

    def sound(self):
        return 'meao meao'

doggy = Dog('boony','pug')
print(doggy.sound())
