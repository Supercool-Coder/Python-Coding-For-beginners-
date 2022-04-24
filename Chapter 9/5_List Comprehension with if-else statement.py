# List comprehension with if-else statement

# This method is normal method to create ( 'even num is +ive and odd num is -ive' )
nums = [1,2,3,4,5,6,7,8,9]

new_list = []
for i in nums:
    if i%2 ==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)

# Driver code
print(new_list)


# This method is a comprehension method to create ( 'even num is +ive and odd num is -ive' )
new_list2 = [i*2 if (i%2 == 0) else -i for i in nums]
print(new_list2)