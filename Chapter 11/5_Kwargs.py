# Kwargs (keyword arguments)
# **Kwargs (double star operator)

# Kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(first_name = 'Uttam', last_name = 'Singh')


def func(**kwargs):
    for u,s in kwargs.items():
        print(f'{u} : {s}')

# dictionary unpacking
d = {'name':'Uttam' , 'last':'Singh' , 'age':20}
func(**d)
# func(first_name = 'Uttam', last_name = 'Singh')