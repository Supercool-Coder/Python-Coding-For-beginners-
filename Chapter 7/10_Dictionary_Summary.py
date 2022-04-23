# Semmary Dictionary

# What is dictionary ?
# Dictionary is a unordered collection of data

# We can create a dictionary in various forms

d = {'name':'Uttam' , 'age':20 }

# ------------- OR ------------

d1 = dict(name = 'Uttam' , age = 20)

# ------------- OR ------------

d2 = {
    'name': 'Uttam',
    'age':20
}


# How to access data from dictionary

# you cannot do like
# d[0] , Because there is no order inside dictionary

# Syntax
# print(dictname[keyname])
print(d['name'])


# Add data inside empty dictionary --- {dict} ?
empty_dict = {}
empty_dict['key 1'] = 'value : 1'
empty_dict['key 2'] = 'value : 2'
print(empty_dict)

# Check existence of values inside dict use in keyword to check for keys
if 'student' in d:
    print('student')


# How to iterate over dictionary most common method
# for key, value in d.items():
#     print(f'key is {key} and value is {value}')


# How to print all keys
# for i in d:
#     print(i)


# Most common dictionary methods

# Get method

# To access a key and check existance
# print(d.get('name'))


# Question ---> Why we use get method ?
# Answer ---> To get rid of error

# For example
# print(d['names'])
# print(d.get('names'))


# To delete item
# pop ---> Take one argument which is keyname

# popped = d1.pop('name')
# print(popped)
# print(d1)



# popitem

popped = d.popitem()
print(popped)
print(d)