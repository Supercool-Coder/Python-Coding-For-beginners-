# List comprehension in nested list

example = [[4,5,6] , [4,5,6] , [6,7,8]]

# This method output comes 4 times [4,5,6,7]
New_list = [[i for i in range(4,8)] for j in range(4)]
print(New_list)


# This output comes six times [4,5,6,7]
new_list2 = []

for i in range(3,9): # This line code is decide how many times come your list

        new_list2.append([4,5,6,7])
print(new_list2)