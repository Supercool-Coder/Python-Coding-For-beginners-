from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        data_type = []
        for arg in args:
            data_type.append(type(arg)==int)
        if all(data_type):
            return function(*args, **kwargs)
        else:
            print('This is a invalid argument....! ')
    return wrapper_function

@only_int_allow
def add_nums(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_nums(5,8,13,10))




# Using list comprehension

from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if ([type(args) ==int for arg in args]):
            return function(*args , **kwargs)
        print('Invalid argument')
    return wrapper_function

@only_int_allow
def add_nums(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_nums(5,8,13,10))

