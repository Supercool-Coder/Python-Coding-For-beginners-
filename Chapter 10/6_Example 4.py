# ---> Conditionals in dictionary comprehension
# ---> We can further customize dictionary comprehension by adding condition to it.

# if condition dictionary comprehension
original_dict = {'Uttam':55,'Ankit':88,'Dinesh':33,'Anurag':98}
even_dict = {k: v for (k,v) in original_dict.items() if v % 2 ==0}
print(even_dict)
# As we can see, only the items with even value have been added, because of the if clause in the dictionary
# comprehension.


# Multiple if conditions dictionary comprehension
original_dict1 = {'Uttam':55,'Ankit':88,'Dinesh':33,'Anurag':98}
new_dict = {k: v for (k,v) in original_dict1.items() if v%2 !=0 if v<60}
print(new_dict)
# In this case, only the items with an odd value of less than 60 have been added to the new dictionary.
# It is because of the multiple if clause in the dictionary comprehension. They are equivalent to and operation where
# both conditions have to be true.


# if-else condition dictionary comprehension
original_dict2 = {'Uttam':55,'Ankit':88,'Dinesh':33,'Anurag':98}
new_dict1 = {k: ('old' if v>60 else 'young') for (k,v) in original_dict2.items()}
print(new_dict1)
# In this case, a new dictionary is created via dictionary compresion.
# The item with a value of 60 or more have the value of 'old' while other have the value of 'young'.