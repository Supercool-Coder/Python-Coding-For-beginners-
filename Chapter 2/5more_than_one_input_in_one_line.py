# # split ----> Split is a string method we will see many more string methods in this chapter
# name = input("Enter the your name sir please")
# age = input("What is your age sir ")
# print(name + age)

name, age = input("Enter the your name sir and your age also enter ").split(",")
print(name)
print(age)

