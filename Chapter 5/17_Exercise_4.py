# Filter odd even
# Define a function
# input
# list---> [1,2,3,4,5,6,7,8,9]
# output ---> [[1,3,5,7,9] , [2,4,6,8]]
def filtter_odd_even(l):
    odd_num = []
    even_num = []
    for i in l:
        if i % 2:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [odd_num , even_num]

    return output
num = [1,2,3,4,5,6,7,8,9]
print(filtter_odd_even(num))