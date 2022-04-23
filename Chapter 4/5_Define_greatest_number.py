# Define greatest number between three numbers
def three_greatest_number(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>a and b>c:
            return b
        return c
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))
biggest=three_greatest_number(num1,num2,num3)
print(f"{biggest} this is greatest number")