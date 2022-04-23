# in Keyword and iteration in dictionary
user_info = {
    'name':'Uttam singh',
    'age':20,
    'prepration':'UPSC Examination prepration',
    'Status':'Singhle'
}



# Check if key exist in dictionary


# if 'Uttam singh' in user_info:
#     print('present')
# else:
#     print('Not present')
# Ye method key ko chech krta hai


# Check if value exist in dictionary  ----> Values method

# if 20 in user_info.values():
#     print('present')
# else:
#     print('Not present')
# Ye method values () ko check krta hai


# Loops in dictionaries

# for i in user_info:
#     print(i)
# ye method user_info naam k variable mein jitne bhi keyword hai wo sare keywords ko print kr dega

# for i in user_info.values():
#     print(i)
# ye method user_info naam k sare values ko present kr  dega

# Values method

# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))
# But these are not lists , you cannot add, delete data from dict values like list, but you can iterate dict values.

# keys method

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# items method

# user_items = user_info.items()
# print(user_items)
# print(type(user_items))


# for loopping
for key , values in user_info.items():
    print(f"kei is : {key} and value is value : {values}")

# tuple unpacking
for i in user_info.items():
    print(i)