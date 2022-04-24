class Laptop:
    def __init__(self,laptop_name,model_name,price):
        # Insatance variables
        self.brand = laptop_name
        self.name = model_name
        self.price = price
        self.full_name = laptop_name + ' ' + model_name

    def apply_discount(self,number):
        offer_price = (number/100)*self.price
        return self.price - offer_price

l1 = Laptop('Lenovo','Ideapad S340',40000)
l2 = Laptop('Dell','Generation 5',80000)
# print(l1.brand,l1.name,l1.price)
print(l1.full_name)
print(l1.apply_discount(10))
print(l2.apply_discount(13))