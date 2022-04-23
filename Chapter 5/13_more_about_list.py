# generate list with range function
# numbers = list(range(1,11))
# print(numbers)


# something more about pop method
# nums = list(range(1,9))
# nums.pop()
# print(nums.pop())
# pop method value ko return bhi krta hai


# index method
num = list(range(1,11))
print(num.index(5))


# pass list to a function
numbers = [1,2,3,4,4,5,5,6]
def positive_list(l):
    positive = []
    for i in l:
        positive.append(i)
    return positive
print(positive_list(numbers))