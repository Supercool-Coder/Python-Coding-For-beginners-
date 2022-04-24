# Map function
def square(a):
    return a**2
l = [1,2,3,4,5]
# print(list(map(square , l)))
print(list(map(lambda a:a**2 , l)))

def my_func(func, l):
    new_list = []
    for i in l:
        new_list.append(func(i))
    return new_list
print(my_func(square , l))


# Using list comprehension
def my_map(func , l):
    return [func(i) for i in l]
print(my_map(lambda a:a**2,l))