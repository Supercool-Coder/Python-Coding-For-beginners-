# This is Challenge

# Define a function take any no of list containing number
# [1,2,3] , [4,5,6] ,[7,8,9]
# return average
# (1,4,7)/3 , (2,5,8)/3 , (3,6,9)/3

# Try to make this anonymous function in one line using lambda
# iss function mein sirf hum do list k average nikal skte hai
def average_finder(l1,l2):
    average = []
    for i in zip(l1,l2):
        average.append(sum(i)/len(i))
    return average
print(average_finder([1,2,3] , [4,5,6]))

# Aagr humko any number of average nikalna hai toh *args k use krna padhega
def average_finder(*args):
    average = []
    for i in zip(*args):
        average.append(sum(i)/len(i))
    return average
print(average_finder([1,2,3] , [4,5,6] , [7,8,9] , [10,11,12]))


# Ek line mein ko code ko solve using with lambda function

average_finder2 = lambda *args:[sum(i)/len(i) for i in zip(*args)]
print(average_finder2([1,2,3] , [4,5,6] , [7,8,9] , [10,11,12]))
