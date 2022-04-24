# *args with normal parameter

# iss method mein hum kitna bhi num ek sath multiply kr skte hai
def multiply_num(*args):
    num = 1
    for i in args:
        num *= i
    return num
print(multiply_num(5,8))