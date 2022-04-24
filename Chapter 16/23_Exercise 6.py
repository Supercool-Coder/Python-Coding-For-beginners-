# Use of inheritance in pyhton

# Inheritance ---> Inheritance is a way of creating a new class for using detailed of an existing class without
# modifying it.
# The newly formed class is a derived class (or child class).
# Similarly, The existing class is a base class (or parent class).

class Love:
    def __init__(self):
        print("Shraddha is ready.....! ")

    def whoisThis(self):
        print("Shraddha is a love of many boy")

    def about(self):
        print("She is sweetheart")

class Shraddha(Love):
    def __init__(self):
        # call superfunction
        # super.__init__()
        print("Shraddha is goodlooking ")

    def whoisThis(self):
        print("She is goodlooking")

    def success(self):
        print("Every failure is a step to success")

love = Shraddha()
love.whoisThis()
love.about()
love.success()