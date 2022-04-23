# function
# [1,2,3,[1,2,]] , input
def count_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
num = [1,2,3,[4,5,6],[7,5,9,9],[23,45,6]]
print(count_list(num))