# practice for loop
# Ask use a number like 12345
# Calculate sum of digits ---> 1+2+3+4+5

num = (input("Enter the number : "))
total = 0
for i in range(0,len(num)):
    total+=int(num[i])
print(total)