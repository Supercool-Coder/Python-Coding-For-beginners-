# Num to string
# Define a function
def num_to_string(l):

# Isme hum int float ki ek aalag list banayenge aur usko hum list , tuple , mein bhi convert kr skte hai
    return [str(i) for i in l if (type(i) == int or type(i) == float or type(i) == list)]
print(num_to_string([True, False, [1,2,3,4], 1, 5.0, 8]))