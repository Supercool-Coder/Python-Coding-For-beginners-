# Question ---> Define a function that take list of string list containing reverse of every string ?

# NOTE :- Use list comprehension because we already did this exercise using normal method

# For Example --->
# l =['abc','def','ghi']
# reverse_string ---> ['cba' , 'fed' , 'ihg']
def reverse_list(l):
    return [name[::-1] for name in l]
print(reverse_list(['Uttam Singh','Chikku Singh']))

def reverse_srt(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
        return new_list
print(reverse_list(['Taj mahal',"kutubmirar"]))