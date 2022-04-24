# Special magic method / Dunder method
# Operator overloading
# polymorphism

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)

    def phone_name(self):
        return f'{self.brand} {self.model}'

    # str and repr method
    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'Phone ({self.brand}, {self.model}, and price is {self.price})'

phone1 = Phone('Apple','iPhone 12 pro',120000)
print(str(phone1))
print(repr(phone1))
# print(phone.__repr__())