# class method as a constructure
class Preson:
    count_instance = 0 # Class variable/ Class attribute

    def __init__(self,name,sir_name,age):
        self.name = name
        self.sir_name =sir_name
        self.age = age


    @classmethod
    def from_string(cls,string):
        first,last_name,age = string.split(',')
        return cls(first,last_name,age)

    @classmethod
    def count_instance(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__}"

    def full_name(self):
        return f"{self.name} {self.sir_name} {self.age}"

    def is_above_18(self):
        return self.age > 18

p1 = Preson('Uttam','singh',20)
p2 = Preson.from_string('Uttam , Bhai , 20')
print(p2.full_name())
print(p1.full_name())