# can we derivedmore than one class from base class ?

# multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()
class Phone: # This is base class and child class
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}....."

class Smartphone(Phone): # This is a drived class and parent class
    def __init__(self,brand_name,model_name,_price,ram,storage,display):
        super().__init__(brand_name,model_name,_price)
        self.ram = ram
        self.storage = storage
        self.display = display

        # This is multilevel inheritance
    def full_name(self):
        return f"{self.brand_name} {self.model_name} price is {self._price}"

class FlagshipPhone(Smartphone):
    def __init__(self,brand_name,model_name,price,ram,storage,display,back_camera,front_camera):
        super().__init__(brand_name,model_name,price,ram,storage,display)
        self.back_camera = back_camera
        self.front_camera = front_camera

phone = Phone('Samsung','M31',17500)
smartphone = Smartphone('Samsung','M31',17500,'6 GB','128 GB','15.5 inch')
flagshipPhone = FlagshipPhone('Samsung','M31',17500,'6 GB','128 GB','15.5 inch','64 MP','32 MP')


print(smartphone.full_name())
print(flagshipPhone)
# This is isinheritance method
# print(help(FlagshipPhone))

# this is a issubclass
# Iska output ture aur false mein aayega q ki  Smartphone jo hai wonphone ko inherate kr raha hai
print(issubclass(Smartphone , Phone))