# Introduction to Generators

# Generations and Iterators

# Generators ---> A generator is a very similar to a function that a generator has parameters,can be called , and
# generators a sequence of values,however , instead of building an array containing all the values and returning them
# all at once , a generator yields the values one at a time , which requires less memory and allows the caller to get
# started processing the first few values immediately. In short ,a generator looks like a function behaves like iterator





# We are going to create our first generator function
# 1). Generator function
# 2). Generator comprehension

# 1). Generator function
def nums(x):
    for i in range(1,x+1):
        print(i)
# nums(11)




# Using yield keyword
def showing_num(s):
    for i in range(1,s+1):


# Yield keyword ---> Yield is a keyword so don't have to write i in parenthesis because it's not a function. I mean we
# can also write as    {'yield i'}   instead of     {'yield(i)'}
        yield(i)


print(showing_num(8))