# All and Any function
def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for i in args:
            total += i
        return total
    else:
        return 'Wrong Input'
print(my_sum(1,2,3,4,8.9))