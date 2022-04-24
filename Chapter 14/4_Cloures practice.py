# function returning function (cloures) practice

# for example----> Humko kisi num k cube , square nikalna hai toh isss function k use kr skte hai .
def to_power(u):
    def cal_power(s):
        return s**u
    return cal_power
cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))