# Show ticket pricing

# 1 to 5 (free)
# 5 to 10 (800)
# 10 to 15 (1800)
# 15 to 100 (2500)
# age = int(input("Enter the your age : "))
# if 0<age<=5:
#     print("Your ticket is --> free")
# elif 5<age<=10:
#     print("your ticket price is ----> 800")
# elif 10<age<=15:
#     print("your ticket priuce is ---> 1800")
# elif 15<age<=100:
#     print("your ticket price is ---> 2500")

marks = int(input("Enter the your marks : "))
if 90<=marks<=100:
    print("You are a topper of our college : ")
elif 80<marks<=90:
    print("You are a topper of our class : ")
elif 70<marks<=80:
    print("you have score good mmarks division : ")
elif 60<marks<=70:
    print("you are pass first also divison : ")
elif 45<marks<=60:
    print("you are second division pass do hard work : ")
elif 34<marks<=45:
    print("your marks is very poor you just pass this year : ")
else:
    print("you are fail try next year best of luck : ")