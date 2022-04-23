# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n
n = int(input("Enetr the any number : "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print(total)