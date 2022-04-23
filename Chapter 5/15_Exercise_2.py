# Define the function which will take list as a argument and its function will return a reversed list

# Example --->
# [1,2,3,4] ---> [4,3,2,1]
# [word 1 , word 2] ---> [word 2 , word 1]

# Note you simply do this with reverse method or [::-1]
# but try to do this with the help of append and return method


# # We are using here "List slicing" method
# def reverse_list(l):
#    l.reverse()
#    return l
# num = [1,2,3,4,5]
# print(reverse_list(num))




# # This is a "string slicing" method
# def reverse_num(l):
#     return l[::-1]
# num = [6,7,8,9]
# print(reverse_num(num))





def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
number = [1,2,3,4,5]
print(reverse_list(number))
