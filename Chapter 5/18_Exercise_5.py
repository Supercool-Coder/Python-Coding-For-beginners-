# Common elements finder function
# Define a function which take 2 lists as input and return a list which contains common elements of lists

# Example
# input ----> [1,2,5,8] , [1,2,7,6]

def common_number(l1 , l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_number([1,2,3,4,5],[1,2,5,4,8,9]))