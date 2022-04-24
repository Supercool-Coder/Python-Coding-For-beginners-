# you have to have a complete understanding of functions,
# first class function/closures
# then finally we will learn about decorators
def square(a):
    return a**2
s = square
print(s(7))

# ye s k naam pata krne k liye hai
print(s.__name__)

# Ye location check krne k liye hai
print(s)
print(square)