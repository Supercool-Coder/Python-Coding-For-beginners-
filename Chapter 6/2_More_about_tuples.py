# Looping in tuples
# Tuples with one element
# Tuples without parenthesis
# Tuples unpacking
# List inside tuples
# Some functions that you can use with tuples

mixed = (1,2,3,4,5.0)
i = mixed

# for loop and tuple
for i in mixed:
    print(i)



# You can use while loop too
# while i:
#     print(i)
#     i += 1


# Tuples with one element
nums  = (5,)
words = ('Uttam bhai')
print(type(mixed))
print(type(nums))
print(type(words))
# hame number k baad { ' comma ' } lagana jaruri hota hai tabhi wo tuple banta hai nhi toh wo element int hi raheta hai


# Tuples withod parenthesis
name = 'Uttam','Dinesh','Ankit','Anurag'
print(type(name))

# Tuple unpacking
movie = ('Ram leela','Gangstar','villan')
movie1 , movie2 , movie3 = movie
print(movie1)


# List inside tuple
favourites = ('southern magnolia',['tokyo Ghoul Theme','landscape'])
favourites[1].pop()
print(favourites)

subjects = ('Optional Mathematics',['General studys 1 ', 'UPSC'])
subjects[1].pop()
subjects[1].append('I will clear Upsc examinition in any condition')
print(subjects)

# min() , max() , sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))