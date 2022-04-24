# Lambda Expression (anonymous function)

# Lambda Expression ---> Lambda Expression ye ek function hai jisko hum ek line mein define kr dete hai iska koi naam
# nhi hota hai .

def add(a,b):
    return a+b

add_num = lambda a,b : a+b
print(add_num(5,8))

# Lambda Expression ko hum  built in , map , reduce , filter in sare function k sath hum use krte hai lambda expression k

multiply = lambda x,y : x*y
print(multiply(5,8))