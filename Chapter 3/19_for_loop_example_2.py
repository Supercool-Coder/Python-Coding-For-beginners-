# Practice for loop
# Ask user a number like 1234
# Calculate sum of digits ----> 1+2+3+4+5
total = 0
num = (input("Enter the number : "))
for i in range(0,len(num)):
    total+=int(num[i])
print(total)