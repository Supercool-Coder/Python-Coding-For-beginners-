# Dry principle ---> Dry principle ye kaheta hai ki kisi bhi line ko dobara nhi likhna chahiye ("don't repeat yourself")



# winning_number = 888
# guess = 1
# number = int(input("Enter the number between 1 to 1000 : "))
# game_over = False
# while not game_over:
#     if number==winning_number:
#         print(f"You Win! , You guess this number in {guess} times")
#         game_over=True
#     else:
#         if number<winning_number:
#             print("Too Low")
#         else:
#             print("Too High")
#
#         guess+=1
#         number=int(input("guess again : \n"))




import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Enter the number between 1 to 100 : "))
game_over = False
while not game_over:
    if number==winning_number:
        print(f"You Win! , You guess this number in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("Too Low")
        else:
            print("Too High")

        guess+=1
        number=int(input("guess again : \n"))