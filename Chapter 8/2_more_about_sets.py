# In keyword in sets and for loop

s = {'u','t','t','a','m'}

# in keyword to check if item is present or not in set
if 's' in s:
    print('Present')
else:
    print('Not Present')

# for loop
for item in s:
    print(item)

# set maths
s1 = {1,2,3,4,5}
s2 = {3,4,5,8,9}

# union ---> Iska mtlb s1 aur s2 mein jo elements common hai uske ek baar hi print krega {3,4,5}
union_set = s1|s2
print(union_set)

# Intersection ---> Iska mtlb s1 aur s2 mein jo elements common hai usko print krega ye method
print(s1&s2)