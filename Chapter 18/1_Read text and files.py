# Methods ---> Read file , Open file , Read method , Seek method , Tell method , Read line , Read lines , Close method

# Read file


# Open function


# Read method
# Ye method hamare cursor ki positon ko change krta hai

# Seek method
# Ye method hamare file ko phir se read krta hai aur cursor ki position ko change bhi krta hai

# Tell method
# Ye method hamare cursor k position ko batata hai


# Readline method
# Ye method hamare file k ek baar mein ek hi line read krta hai

# Readlines method
# Ye method hamare file k sare line ko ek list me add kr dega aur hum jitni lines chahte hai utni lines ko read kr skte
# hai iss method k use kr k.

# Close method

f = open('file.txt')
# print(f'cursor position - {f.tell()}')
#
# print(f.read())
# print(f'cursor position - {f.tell()}')
# print('Before seek method :- ')
# f.seek(0)
# print('After seek method :- ')
# print(f'cursor position - {f.tell()}')
# print(f.read())
# f.close()


# Readline method


# f = open('file.txt')
#
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())


# Readlines method

# lines = f.readlines()
# print(len(lines))
# for line in lines:
#     print(line , end='')

# Close method
print(f.closed)
f.close()