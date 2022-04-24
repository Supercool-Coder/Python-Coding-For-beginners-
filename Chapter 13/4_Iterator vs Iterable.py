# Iterator vs Iterables

numbers = [1,2,3,4,5] # tuples , string ---> iterables
square = map(lambda a:a**2 , numbers) # iterator

# aagr humko direct iterator function call krna hai toh
# ye function bs iterator k liye hi kaam krta hai iterables k liye ye function kaam nhi krega
print(next(square))
print(next(square))
print(next(square))
# print(next(square))
# print(next(square))





# for loop aise kaam krta hai run krne pr
# for i in numbers:
#     print(i)
# numbers_iter = iter(numbers)
# print(next(numbers_iter))
# print(next(numbers_iter))
# print(next(numbers_iter))
# print(next(numbers_iter))
# print(next(numbers_iter))