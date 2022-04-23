# Dictionaries introduction
# Question ---> Why we use Dictionaries?
# Answer ---> Because of limitations of lists , lists are not enough to represent real data .

# Example
# user =['Uttam singh',20['bhag milkha bhag' , 'MS Dhoini untold story'],['masaqkali','jastin biber']]
# This list contains user name , age , favorate movie , favorate ringtones
# You can also do this but this is not a good way to do this.

# Question ---> What are dictionaries ?
# Answer ---> Unordered collection od data in key : value pair .

# How to create dictionaries ?
# user = {'name' : 'Uttam singh','age':20,'favorate movie':'bhag milkha bhag'}
# print(user)
# print(type(user))

# Second method to create dictionary ?
name = dict(name = 'Uttam Singh' , age = 20)
print(name)

# How to access data from dictionary ?
# Note = There is no indexing because of unordered collection of data .
print(name['name'])
print(name['age'])


# Question ---> Which type of dectionary can store ?
# Answer ---> Any type of data we can storein dictonary
# Example ---> Number , Strings , List , Dictionary

user_info = {
    'name':'Uttam singh',
    'age':20,
    'prepration':'UPSC Examination prepration',
    'Status':'Singhle'
}

print(user_info['Status'])


# How to add data to empty dictonary ?
user_info2 = {}
user_info2['successfull'] = 'Hardwork is the soluation to success'
user_info2['time '] = 'Time management is the most to prefectly complete any work'
print(user_info2)