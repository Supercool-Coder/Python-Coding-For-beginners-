# 1). Encapsulation ---> Encapsulation means apne data ko aur uss data k sath aap jo functionality perform krte hai use
# hi encapsulation bolte hai.


# 2). Abstraction ---> Abstraction means complaxility ko sort krna (hide krna) "Jab tk ecapsulation nhi hoga tb tk hi
# abstraction bhi nhi hoga


# 3). Some special naming convention ---> (underscore name_) underscore ek convention hai iska use kisi kisi "private
# name" k liye kiya jata hai aur ye batane kiya bhi kiya jata hai ki uss naam se koi chedh chadh na kre


# 4). Name mangling ---> this is not a convention isme hum double underscore use krte hai "isme python name change krta hai "
# Dunder/Magic methods k mtlb hota hai (double underscore ---> __name__)

class Phone:
    def __init__(self,Model,brand,price):
        self.Model = Model
        self.Brand = brand
        self.__Price = price

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number} ....")

    def full_name(self):
        return f"{self.Brand} {self.Model}"

p1 = Phone('Samsung galaxy m31','Samsung',17500)
# print(p1.__Price)
print(p1.__dict__)