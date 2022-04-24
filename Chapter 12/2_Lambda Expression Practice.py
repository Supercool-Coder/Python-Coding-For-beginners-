# Lambda Expression Pratice
def is_even(a):
    return a%2 == 0
print(is_even(7))

isodd = lambda a : a%2 != 0
print(isodd(3))

def last_char(s):
    return s[-1]
print(last_char('Uttam singh'))

last_char2 = lambda s : s[-1]
print(last_char2('Uttam'))


# Lambda with if , else
def func(s):
    if len(s) > 5:
        return True
    return False

print(func('abcdsdf'))

# using lambda function
function = lambda s : True if len(s) < 5 else False
print(function('1234e5'))

# withod using if else
function = lambda s : len(s) < 5
print(function('1235'))
