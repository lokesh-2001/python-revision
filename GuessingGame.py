# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they 
# guessed too low, too high, or exactly right. 
import random
rd = random.randint(1,9)
guess = 0
c = 0
while guess!=rd and guess!="exit":
    guess = input("Guess the Number: ")
    if guess == "exit":
        break
    guess  = int(guess)
    c+=1
    if guess == rd:
        print("Correct Moves Used: ", c)
    elif guess > rd:
        print("High")
    else:
        print("Low")
