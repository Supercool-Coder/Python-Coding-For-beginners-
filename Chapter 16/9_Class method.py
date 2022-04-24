# class method
# different between class method and instance method
class Person:
    count_instance = 0
    def __init__(self,name,sir_name,age):
        Person.count_instance += 1
        self.Name = name
        self.Sir_name = sir_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instance of {cls.__name__} class....... :-"

    def full_name(self):
        return f"{self.Name}  {self.Sir_name}"

    def above_18(self):
        return self.age>18

name1 = Person('Uttam','Singh',20)
name2 = Person('Ravi','Singh',16)
print(Person.count_instances())