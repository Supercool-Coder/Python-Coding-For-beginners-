# Function with all parameters
# Very important to understand

# PADK ===> P--->Parameter , A---> *args , D--->Default parameter , K---> **kwargs
def func(name = 'unknown' , age=19):
    print(name)
    print(age)
func('Uttam Singh',20)


def func(name , *args , last_name = 'unknown' , **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Uttam', 5,8,13,10, u = 5 , s = 8)