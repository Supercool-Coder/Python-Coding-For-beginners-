# List Comprehension
# with the help of list comprehension we can create of list in one line

# Create a list of squares from 1 to 10
# This is a simple method to create cube
cube = []
for i in range(1,8):
    cube.append(i**3)
print(cube)


# using list comprehension method
cube2 = [i**3 for i in range(9,14)]
print(cube2)



# using simple method to create negative numbers
negative1 = []
for i in range(11,21):
    negative1.append(-i)
print(negative1)

# using list comprehension method
negative = [-i for i in range(1,11)]
print(negative)


# using simple method
names = ['Uttam singh','Chikku singh','Ranvir singh','Sumit singh','Ravi singh']
new_name_list = []
for name in names:
    new_name_list.append(name[0])
print(new_name_list)


# using list comprehension method
new_name_list1 = [name[0] for name in names]
print(new_name_list1)