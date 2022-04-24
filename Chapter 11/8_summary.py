# Iss method mein hum bs do number k hi sum kr skte hai
def add(a, b):
    total = 0
    for num in a,b:
        total += num

    return total

print(add(5,8))


# iss metrhod mein hum unlimited number k sum kr skte hai
def new_add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(new_add(1,2,3,4,5))


# Unpacking method k mtlb hota hai ki aagr hum koi list pass kr rahe hai toh wo list print nhi hota use unpack krne k
# liye * k use krna padhta hai aur isme hum numbers hi print krwa skte hai aur isme jo value aayega wo tuple mein aayega
def addition(*args):
    total = 0
    for i in args:
        total += i
    return total

# ab humko yaha pr dhyan dena padega humne ek list create kr liya hai
l = [1,2,3,4,5,6]
# l k aage * lagana jaruri hai nhi toh ye l ko print nhi krega q ki
print(addition(*l))


# Kwargs --->  keyword argument , ** ("Iss method mein hum dobule star ** lagate hai") isme hum unlimited string ko
# print krwa skte hai aur isme jo value aayega wo dictionary mein aayega
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(Name = 'Uttam', last_name = 'Singh', age = 20)


# kwargs , args , normal , default aagr humko insab ko ek sath use krna hai toh aise krenge hum
def function(name , *args , last_name = 'Unknown' , **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

function('Uttam' , 1,2,3,4 , s = 8 , u = 5)