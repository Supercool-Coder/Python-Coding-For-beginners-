# Using Map function
numbers = [1,2,3,4,5]

def square(a):
    return a**2
squares = tuple(map(square , numbers))
print(squares)


# without using map function
squares_new1 = list(map(lambda a:a**2, numbers))
print(squares)


# Using list comprehension
squares_new2 = [i**2 for i in numbers]
print(squares_new2)


# using appendm function
new_list = []
for num in numbers:
    new_list.append(square(num))

print(new_list)


names = ['abc','absd','abcde','abcdef']
length = list(map(len , names))
print(length)