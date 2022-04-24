class Mobile:
    def __init__(self,name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be object of mobile class')

oneplus = Mobile('One plus 6')
samsung = 'Samsung galaxy M31'
mobostore = Mobilestore()
# print(mobostore.mobiles)

mobostore.add_mobile(oneplus)
mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)