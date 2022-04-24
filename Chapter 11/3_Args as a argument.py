# Args as a argument
def multiply_num(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

nums = [2,3,4]
print(multiply_num(*nums))