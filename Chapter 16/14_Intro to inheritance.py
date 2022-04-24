class Phone: # Base class / Parent class
    def __init__(self,brand,model_name,price):
        self.brand_name = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"

    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ......")


class Smartphone(Phone): # Derived class / Child class
    def __init__(self,brand,model_name,price,ram,SSD,rear_camera):
        # self.brand_name = brand
        # self.model_name = model_name
        # self._price = max(price,0)
        Phone.__init__(self,brand,model_name,price)
        self.Ram =ram
        self.internal_storage = SSD
        self.camera=rear_camera

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"

    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ......")

phone1 = Phone('nokia','1100',1000)
smartphone = Smartphone('Samsung galaxy','M31',17500,'6 GB','128 GB','65 MP')
print(smartphone.brand_name)
print(phone1.brand_name)