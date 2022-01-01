# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
# user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
# correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
# “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track
# of the number of guesses the user makes throughout teh game and tell the user at the end.
# Say the number generated by the computer is 1038. An example interaction could look like this:
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

import random
def func (no, guess):
    cowbull = [0,0] # cow,bull
    for i in range(len(no)):
        if(no[i] == guess[i]):
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

play = True
no = str(random.randint(0,9999))
# print(no)
guess = 0

while play:
    userGuess = input("Guess: ")
    if userGuess == "exit":
        break
    # guess = int(guess)
    count = func(no,userGuess)
    guess+=1
    print("You have "+ str(count[0]) + " cows, and " + str(count[1]) + " bulls.")
    if count[1] == 4 :
        play = False
        print("You win the game after " + str(guess) + "! The number was "+str(no))
        break
    else:
        print("Your guess isn't quite right, try again.")        
