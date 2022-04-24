# List comprehension summary

# What is list comprehension ?

# This is one line program to print the square of numbers
square = [i**2 for i in range(11,21)]
print(square)

square2 = []
for i in range(1,11):
    square2.append(i**3)
print(square2)


# {
# This methos is to print all even number
even_num = [i for i in range(1,11) if i%2 == 0 ]
print(even_num)

# This method is print true false if num is even then print true other wise false
even_num2 = []
for i in range(1,11):
    even_num2.append(i%2 ==0)
print(even_num2)

even = []
for i in range(1,11):
    if i%2 ==0:
        even.append(i)
print(even)

# }

# This method is print inside 1 to 40 all even and odd num with +ive and -ive symbol even is +ive and -ive is odd
mixed_num = [i*2 if i%2 ==0 else -i for i in range(1,21)]
print(mixed_num)

# This method is print nested comprehension list
n1 = [[1,2,3],[1,2,3],[1,2,3]]
new_list1 = [[i for i in range(1,4)]for m in range(3)]
print(new_list1)

# This method is normal to print nested comprehension list
new_list2 = []
for i in range(4):
    new_list2.append([2,3,4])
print(new_list2)