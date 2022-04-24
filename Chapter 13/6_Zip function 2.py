# How to use *star operator with zip function
l1 = [1,21,3,14,5]
l2 = [6,7,8,9,10]
greater_number = []
for i in zip(l1,l2):
    greater_number.append(max(i))
print(greater_number)


# isko hum is formate mein print krwayenge l1 = [1,3,5,7,9] aur l2 = [2,4,6,8,10]
# l = [(1,2),(3,4),(5,6),(7,8),(9,10)]
# l1 , l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))