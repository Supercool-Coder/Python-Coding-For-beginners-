# Make flexible functions

# *operator
# *args


def total(a,m):
    return a+m

# aagr hum 3,4 k aalawa koi aur num dalenge toh error aayega isme
print(total(3,4))

def all_nums(*args):
    print(args)
    print(type(args))


# iss method mein hum kitna bhi number print krwa skte hai
all_nums(1,2,3,34,5,6,67)


# iss method mein hum kitna bhi num ko add kr skte hai
def total_num(*args):
    num = 0
    for i in args:
        num += i
    return num
print(total_num(1,2,3,4,5,6))