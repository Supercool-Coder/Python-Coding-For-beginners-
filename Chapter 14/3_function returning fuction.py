# This method is called function returning function that means one function is return another function value
def outer_func():
    def inner_func():
        print('Hello sir ! how are you...?')
    return inner_func
var = outer_func()
var()

def outer_func2(massg):
    def inner_func():
        print(f'Massage is {massg}')
    return inner_func
devil = outer_func2('I am fine what about you bro....?')
devil()