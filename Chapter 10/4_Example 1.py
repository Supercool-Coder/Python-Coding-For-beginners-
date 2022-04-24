# Ques ---> Python dictionay comprehension ?
# Answ ---> Dictionaries are data types in python which allows us to store data in key/value pair

my_dict = {1: 'Kivi',2:'Orange'}
print(my_dict)

# Ques ---> What is dictionary comprehension in python ?
# Answ ---> Dictionary compresion is an elegant and concise way to create dictionaries

# {
square_dict = dict()
for num in range(1,11):
    square_dict[num] = num*num
print(square_dict)


square_dict1 = {num:num*num for num in range(1,11)}
print(square_dict1)

# }
# The output of both program will be same.

