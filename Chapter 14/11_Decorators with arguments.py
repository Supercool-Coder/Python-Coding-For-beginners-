from functools import wraps
def only_string_data_type_allow(data_type):
    def decorators(function):
        @wraps(function)
        def wrapper_function(*args ,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args , **kwargs)
            print('Invalid argument')
        return wrapper_function
    return decorators

@only_string_data_type_allow(str)
def only_strings_allowed(*args):
    string = ''
    for i in args:
        string += i
    return string
print(only_strings_allowed('Uttam','Singh'))