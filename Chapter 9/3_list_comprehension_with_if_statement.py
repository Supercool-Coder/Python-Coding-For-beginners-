# List compreshenion with if statement

numbers = list(range(1,11))

# print(numbers)
# print(type(numbers)
nums = []
for i in numbers:
    if i%2 ==0:
        nums.append(i)
print(nums)



even_nums = [i for i in numbers if i%2 == 0]
print(even_nums)


odd_nums = []
for i in numbers:
    if i%2 !=0:
        odd_nums.append(i)
print(odd_nums)

odd_nums2 = [i for i in range(1,51) if i%2 !=0]
print(odd_nums2)