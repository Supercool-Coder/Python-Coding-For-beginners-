# Add and delete data
user_info = {
    'name':'Uttam singh',
    'age':20,
    'prepration':'UPSC Examination prepration',
    'Status':'Singhle',
    'Course':'Bachlar of science information techonology'
}

# How to add data
user_info['Course'] = ['This course is a goood cairare oporchunity']
print(user_info)

# How to use pop method
popped_item = user_info.pop('Course')
print(type(popped_item))
print(f"popped item {popped_item}")


# popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))