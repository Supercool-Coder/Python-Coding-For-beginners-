# Create a laptop attributes like brand name , model name ,price
# Create two objects/instance of your laptop class
class Laptop:
    def __init__(self,laptop_name,model_name,price):
        # Insatance variables
        self.brand = laptop_name
        self.name = model_name
        self.price = price
        self.full_name = laptop_name + ' ' + model_name

l1 = Laptop('Lenovo','Ideapad S340',40000)
# print(l1.brand,l1.name,l1.price)
print(l1.full_name)