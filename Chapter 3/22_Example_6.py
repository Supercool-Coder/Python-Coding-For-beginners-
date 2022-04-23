# Modify number Gussing Game
winning = 55
guess = 1
num = int(input("Guess a number between 1 to 100 : "))
game_over = False
while not game_over:
    if num == winning:
       print(f"you win! and you guessed this number in {guess} times")
       game_over=True
    else:
      if num< winning:
         print("Too low : ")
         guess+=1
         num = int(input("guess again : "))
      else:
          print("Too hingh : ")
          guess += 1
          num = int(input("guess again : "))