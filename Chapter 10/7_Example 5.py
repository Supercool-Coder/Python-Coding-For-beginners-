# Nested dictionary with two dictionary comprehension.
dictionary = {
    k1: {k2: k1*k2 for k2 in range(1,11)} for k1 in range(2,4)
}
print(dictionary)


# As you can see, we have constructed a multiplication table in a nested dictionary for number 2 to 4.

# When ever nested dictionary comprehension is used, python first starts form the outer loop and then goes to the inner
# one.

# So, the above code would be equivalent to:

dictionary = dict()
for k1 in range(2,4):
    dictionary[k1] = {k2:k1*k2 for k2 in range(1,11)}
print(dictionary)


dictionary1 = dict()
for k1 in range(2,4):
    dictionary1[k1] = dict()
    for k2 in range(1,11):
        dictionary1[k1][k2] = k1*k2
print(dictionary1)

# All these three programs give us the same output.