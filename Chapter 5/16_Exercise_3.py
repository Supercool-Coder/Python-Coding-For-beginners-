# Define a fuction that take list of words as argument and return list with reverse of every element in that list

# Example ---> [xyz , abc , pqr] ---> [rqp , cba , zyx]

# This is a list string method
# def reverse_name(n):
#     return n[::-1]
# name = ['uttam' , 'shraddha' , 'singhs']
# print(reverse_name(name))




# This is pop and append method
# def reverse_name(N):
#     n_name = []
#     for i in range(len(N)):
#         popped_item = N.pop()
#         n_name.append(popped_item)
#     return n_name
# name = [input("Please enter the your first name sir/miss : ")]
# print(reverse_name(name))


def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
name = ['uttam' , 'shraddha' , 'singh']
print(reverse_elements(name))