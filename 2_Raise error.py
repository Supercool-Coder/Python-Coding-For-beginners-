def add_nums(a,b):
    if (type(a) is int and type(b) is int):
        return a+b
    raise TypeError('OOps you are passing wrong data type......')
print(add_nums('5','8'))