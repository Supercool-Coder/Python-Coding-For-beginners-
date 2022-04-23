# Split method
# convert string to list
user_info = 'uttam singh 23'.split()
print(user_info)

name , age , college = input('Enter the your name and age and college name : ').split(',')
print(name)
print(age)
print(college)


# join method
# converted string to list
user_info = ['uttam singh',  '20']
print('_'.join(user_info))