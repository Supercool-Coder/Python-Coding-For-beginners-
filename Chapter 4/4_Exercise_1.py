# Define  a functon which takes two number as a input and return greater of two numbers. ?

# This is the my soluation and this soluation is not correct
# def greater_num(a,b):
#     if a>b:
#         return "a is the greater than b"
#     return "b ia the greater then a"
# print(greater_num(15,16))

# def greater_num(a,b):
#     if a>b:
#         return a
#     return b
# num1= int(input("Enter the first number : "))
# num2= int(input("Enter the second value : "))
# print(greater_num(num1,num2))

def greater_num(a,b):
    if a>b:
        return a
    return b
num1= int(input("Enter the first number : "))
num2= int(input("Enter the second value : "))
bigger_number = greater_num(num1,num2)
print(f"{bigger_number} is the greates number")