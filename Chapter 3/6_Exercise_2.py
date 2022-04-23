# Exercise ---> Watch Coco
# Ask user,s name and age
# if user,s name start with ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# else print sorry you can't watch this movie

name = input("Enter the your name : ")
age = int(input("Enter your age : "))
if age >= 14 and name[0] == "U" or name[0] == 'u':
    print("You can watch coco movie : ")
else:
    print("You can not watch coco movie  : ")