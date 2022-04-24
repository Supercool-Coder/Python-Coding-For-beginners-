# Decorators ---> Enhance the functionality of other functions
# @ ---> Use for decorators function
def decorators_function(anyfunction):
    def wrapper_function():
        print('This is a awesome function .....')
        anyfunction()
    return wrapper_function

@decorators_function # This is a short cut method to call decorator function.
def func1():
    print('This is a function 1')
func1()


# @decorators_function
def func2():
    print('This is function 2')
func2 = decorators_function(func2)
func2()
