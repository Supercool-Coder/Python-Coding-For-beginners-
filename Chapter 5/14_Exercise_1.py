# Define a function which will take list containing numbers as input and return list containing square of every
# elements

# for example
# numbers ---> [1,2,3,4]
# square_list(numbers) ---> return ---> [1,4,9,16]

def filter_odd_even(l):
    odd_num = []
    even_num = []
    for i in l:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [odd_num , even_num]
    return output
num = [1,2,3,4,5,6,7,8,9,10,11]
print(filter_odd_even(num))

