# Question --> Ask user to input 3 numbers and you have to print average of three numbers using string formatting ?
# Bonus:- Try to take all three comma separated inputs in one line.

# first soluation
number1 = int(input("Enter the three number : "))
number2 = int(input("Enter the three number : "))
number3 = int(input("Enter the three number : "))
total = number1 + number2 + number3
print(total / 3)

# second soluation
number1 = int(input("\nEnter the three number : "))
number2 = int(input("Enter the three number : "))
number3 = int(input("Enter the three number : "))
print(f"average of three numbers : {(int(number1) + int(number2) + int(number3)) / 3}\n")

# Bonus soluation
num1, num2, num3 = input("\nEnter the three numbers comma seprated : ").split(",")
print(f"average of three numbers : {(int(number1) + int(number2) + int(number3)) / 3}")