def decorators_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('This is a awesome function')
        return any_function(*args,**kwargs)
    return wrapper_function

@decorators_function
def func(q):
    print(f'This is a function with argument {q} ')
func(5)

@decorators_function
def add_nums(x,y):
    return x+y

print(add_nums(5,8))