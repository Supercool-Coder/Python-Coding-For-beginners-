class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def cal_circumference(self):
        return 2*Circle.pi*self.radius

c1 = Circle(5)
c2 =Circle(8)
print(c1.cal_circumference())





class Bike:
    discount =10
    def __init__(self,name , color, speed,price):
        self.Name = name
        self.Color = color
        self.Speed = speed
        self.Price = price

    def bike_discount(self):
        offer = (Bike.discount/100)*self.Price
        return self.Price - offer

P1 = Bike('Palsaur','Black and Blue' , 220 , 220000)
print(P1.bike_discount())