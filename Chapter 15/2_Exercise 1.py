# Define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number
def even_sequence(x):
    # sequence = []
    for i in range(1,x+1):
        if i%2==0:
            yield (i)


print(even_sequence(10))

for i in even_sequence(10):
    print(i)