# Using list comprehension
square = [i**2 for i in range(1,11)]
print(square)

# Using generator comprehension
cube = (i**3 for i in range(1,6))
# print(cube)
for i in cube:
    print(i)