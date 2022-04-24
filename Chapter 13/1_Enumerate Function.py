# We use enumerate function with for loop to track position of our item in iterable


# How we can do this withod enumerate function
names  = ['uttam' , 'singh' , 'Dinesh' ,'Padhi' , 'Ankit' , 'Patwa' , 'Anurag' , 'sigu']
# position = 0
# for name in names:
#     print(f'{position} ---> {name}')
#     position += 1


# with enumerate function
# for pos , name in enumerate(names):
#     print(f'{pos} ---> {name}')


# Define a function that take two arguments
# 1). List containing string
# 2). String that want to find in your list
# and this function will return the index of string in your list and if string is not present then retur -1

def func_pos(l,target):
    for pos , name in enumerate(l):
        if name == target:
            return pos
    return -1

print(func_pos(names,'Ankit'))