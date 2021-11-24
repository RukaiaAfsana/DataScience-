import random, sys
wins=0
loses=0
ties=0
while 1:
    print("ROCK ,PAPER,SESSIOR\n")
    print("wins: {}, loses:{} , ties:{}".format(wins,loses,ties))
    while 1:
        print("Please enter your choice. r for ROCK, p FOR Paper, s for Sessior and q for quit the game")
        playerinput = input()
        if playerinput == "r" or playerinput == "p" or playerinput == "s":
            break
        elif playerinput == "q":
            sys.exit()
        else:
            print("please select r/p/s")

    if playerinput == "r":
        print("Rock verses..")
    elif playerinput == "p":
        print("Paper verses..")
    else :
        print("Sessior verses..")

    computerstring = "rps"
    computerinput = random.choice(computerstring)

    if computerinput == "r":
        print("Rock")
    elif computerstring == "p":
        print("Paper")
    elif computerinput =="s":
        print("Sessior")

    if computerinput == playerinput:
        print("it's a tie !!!\n")
        ties=ties+1
    elif computerinput =='p' and playerinput =='r':
        print("YOU lose\n")
        loses=loses+1
    elif computerinput =='s' and playerinput =='r':
        print("YOU wins\n")
        wins=wins+1
    elif computerinput =='r' and playerinput =='s':
        print("YOU lose\n")
        loses=loses+1
    elif computerinput =='p' and playerinput =='s':
        print("YOU wins\n")
        wins=wins+1
    elif computerinput =='r' and playerinput =='p':
        print("YOU wins\n")
        wins=wins+1
    elif computerinput =='s' and playerinput =='p':
        print("YOU lose\n")
        loses=loses+1
