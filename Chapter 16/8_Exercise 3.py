class Person:
    count_instance = 0
    def __init__(self,Name , Graduation , Age, Skills):
        Person.count_instance += 1
        self.Name = Name
        self.Degree = Graduation
        self.Age = Age
        self.Skills = Skills

B1 = Person('Uttam Singh','BSC.IT',20,'Python , ML&AI')
B2 = Person('Uttam Singh','BSC.IT',20,'Python , ML&AI')
B3 = Person('Uttam Singh','BSC.IT',20,'Python , ML&AI')
B4 = Person('Uttam Singh','BSC.IT',20,'Python , ML&AI')
B5 = Person('Uttam Singh','BSC.IT',20,'Python , ML&AI')

print(Person.count_instance)