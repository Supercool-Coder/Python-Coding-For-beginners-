# Instance method and Object method both are samething

class Person:
    def __init__(self,name,sir_name,age):
        self.Name = name
        self.Sir_name = sir_name
        self.age = age

    def full_name(self):
        return f"{self.Name}  {self.Sir_name}"

    def above_18(self):
        return self.age>18

name1 = Person('Uttam','Singh',20)
name2 = Person('Ravi','Singh',16)
print(name1.full_name())
print(name2.above_18())