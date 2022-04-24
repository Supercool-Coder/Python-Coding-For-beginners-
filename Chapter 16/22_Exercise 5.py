# Creating methods in python

# Methods ---> Methods are function defined inside the body of a class. They are used to defined the behaviors of an
# object.
class Shraddha:
    # Instance attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Instance method
    def sing(self,song):
        return f"{self.name} is singing {song}"

    def dance(self):
        return f"{self.name} is dancing now.....! "

# Insatatiate the object
love = Shraddha("Shraddha",20)

# Call our instance methods
print(love.sing("She is very happy now.....  :): "))
print(love.dance())