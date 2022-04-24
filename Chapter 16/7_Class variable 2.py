class Bike:
    discount =10
    def __init__(self,name , color, speed,price):
        self.Name = name
        self.Color = color
        self.Speed = speed
        self.Price = price

    def bike_discount(self):
        # hum class k naam tb use krenge jab sare products k liye discount dena ho
        # offer = (Bike.discount / 100) * self.Price
        offer = (self.discount/100)*self.Price
        return self.Price - offer



P1 = Bike('Palsaur','Black and Blue' , 220 , 220000)
P2 = Bike('Aapachi','Black',240,180000)
P3 = Bike('Hero Honda','Black',180,70000)


P1.discount = 50
print(P1.__dict__)
print(P1.bike_discount())