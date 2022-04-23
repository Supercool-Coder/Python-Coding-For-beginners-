# Exercise , Number Gussing Game
# Make a variable, like winning number and assign any number to it.
# Ask user to guess a number.
# if user guessed correctly then print "YOU WIN !!!!"


# if user didn't correct then :-
   # if user guessed lower than actual number then print "Too Low"
   # if user guessed higher than actual number then print "Too High"


# Google "how to generate random number in python" to generate random
# Winning number

winning_number = 555
user_number = int(input("Enter a number Between 1 to 1000 : "))
if user_number == winning_number:
    print("You Win !!!!!")
else:
    if user_number < winning_number:
        print("TOO LOW Better Luck try next time !!!!!")
    else:
            print("TOO HIGH Better luck try next time !!!!!")
