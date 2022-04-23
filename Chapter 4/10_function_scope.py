# Scope

# x=5
#
# def func(x):
#     x=8
#     return x
#
# print(func(x))
# print(x)

x=5 # global variable

def func():
    global x
    x=8 # local variable
    return x
print(x)
print(func())
print(x)