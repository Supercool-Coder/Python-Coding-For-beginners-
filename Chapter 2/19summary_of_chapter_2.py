# string
name = "Uttam singh"

# string indexing
print(name[4])

# string slicing
print(name[0:7])
print(name[::-1])
print(name[-1:12:2])

# Take user input
name, age = input("enter the your name and age : ").split(",")
print(name)
print(age)

# length function
print(len(name))

# lower , upper , title method
print(name.lower())
print(name.upper())
print(name.title())

# find ,replace, center method
print(name.find("t"))
print(name.center(15,"*^"))
print(name.replace("s","S"))

# string are immutable
string.replace("s","S")
print(string)