while True:
    game = {'rock': 1,'scissor' : 2,'paper':3}
    player1 = str(input("Enter Move (player 1): ")) 
    player2 = str(input("Enter Move (player 2): "))
    move1 = game.get(player1) 
    move2 = game.get(player2) 
    dif  = move1 - move2
    if dif in [-1,2]:
        print("player 1 wins: ")
        if(str(input("wanna continue: ")) == 'yes'):
            continue
        else:
            print("game over")
            break
    elif dif in [-2,1]:
        print("player 2 wins: ")
        if(str(input("wanna continue: ")) == 'yes'):
            continue
        else:
            print("game over")
            break
    else:
        print("draw")


