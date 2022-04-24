# Filter Function
def is_even(a):
    return a%2 ==0

numbers = [3,2,1,10,6,4,5,7,9,8]
# evens = tuple(filter(is_even , numbers))
evens = filter(lambda a:a%2 ==0 , numbers)
print(evens)
