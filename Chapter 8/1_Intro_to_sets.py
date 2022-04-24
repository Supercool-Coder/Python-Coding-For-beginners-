# Set data type
# Unordered collection of unique items

# we cannot store list and dictionary in set


s = {1,2,3,4,5,5}
# print(s)
# l = [1,2,3,3,4,5,5,6,6,7,8,8,7,4,7,6,5,2,9,9,10,10]

# Remove Duplicate

# This is a set
# s2 = set(l)

# This is a list
# s2 = list(set(l))

# print(s2)
# print(type(s2))


# Add method in sets
s.add(6)
print(s)

# Remove method in sets
s.remove(6)
print(s)

# Discard method in sets
# Iss method mein value rahega toh use delete kr dega list se nhi hoga toh nhi krega delete lekin error nhi aayega
s.discard(7)
print(s)

# Clear method in sets
s.clear()
print(s)

# Copy method in sets
s1 = s.copy()
print(s1)



# we cannot store list and dictionary in set
# Set mein    unique items ---> (iska mtlb 1 number do baar print nhi hoga sets mein)
s2 = {1,2.0,'uttam singh',5,8,'eight'}
print(s2)