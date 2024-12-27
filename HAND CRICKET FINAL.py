import random as r
wins=0
losses=0
while True:
    c=int(input("If you would like to play enter one(1); if you would like to exit click (2):"))
    print()
    if c==1:
        overs=6*(int(input("How many overs would you like to play for?")))
        print()
        toss=int(input("wonderful, now as for the toss, heads(1) or tails(2):"))
        print()
        coin=r.randint(1,2)
        if toss!=1 and toss!=2:
            print("Wrong Call!")
            print()
        else:
            if toss==coin:
                choice=int(input("Congratulations, you just won the toss would you like to bat(1)or bowl(2):"))
                if choice==1:
                    pruns=0
                    cruns=0
                    print("You chose to bat!")
                    i=0
                    while i<overs:
                        print()
                        bat=int(input("How many runs would you like to go for"))
                        ball=r.randint(1,6)
                        if bat==ball:
                            print("OPPS!, you are out and you scored a total of",pruns)
                            break
                        elif bat!=ball and bat<7:
                            print("Nice shot!, you scored",bat,"runs and now have",pruns+bat,"runs in total")
                            pruns+=bat
                            i+=1
                        elif bat>=7:
                            print("You cant score 7 or more runs, try again")
                            i+=1
                    i=0
                    while i<overs:
                        print()
                        bat=r.randint(1,6)
                        ball=int(input("How many runs do you think they will go for?"))
                        if bat==ball:
                            print("Well done! opponent is now out")
                            break
                        elif bat!=ball and bat<7:
                            print("So close, your opponent scored",bat,"runs and now they have",cruns+bat,"runs in total")
                            cruns+=bat
                            i+=1
                        elif ball>=7:
                            print("Bad ball :( opponent scored ",bat,"runs and now has",cruns+bat)
                            cruns+=bat
                            i+=1
                        if cruns>pruns:
                            break
                    print()
                    print("In the end you had",pruns,"and the computer had",cruns)
                    print()
                    if pruns>cruns:
                        print("You won by",pruns-cruns)
                        wins+=1
                    elif cruns>pruns:
                        print("You lost by",cruns-pruns,", better luck next time")
                        losses+=1
                elif choice==2:
                    pruns=0
                    cruns=0
                    print("You chose to bowl!")
                    i=0
                    while i<overs:
                        bat=r.randint(1,6)
                        print()
                        ball=int(input("How many runs do you think they will go for?"))
                        if bat==ball:
                            print("Well done! opponent is now out")
                            break
                        elif bat!=ball and bat<7:
                            print("So close, your opponent scored",bat,"runs and now they have",cruns+bat,"runs in total")
                            cruns+=bat
                            i+=1
                        elif ball>=7:
                            print("Bad ball :( opponent scored ",bat,"runs and now has",cruns+bat)
                            cruns+=bat
                            i+=1
                    i=0
                    while i<overs:
                        print()
                        bat=int(input("How many runs would you like to go for"))
                        ball=r.randint(1,6)
                        if bat==ball:
                            print("OPPS!, youre out and you scored a total of",pruns)
                            break
                        elif bat!=ball and bat<7:
                            print("Nice shot, you scored",bat,"runs and now have",pruns+bat,"runs in total")
                            pruns+=bat
                            i+=1
                        elif bat>=7:
                            print("You cant score 7 or more runs, try again")
                            i+=1
                        if pruns>cruns:
                            break
                    print()
                    print("In the end you had",pruns,"and the computer had",cruns)
                    if pruns>cruns:
                        print("You won by",pruns-cruns)
                        wins+=1
                    elif cruns>pruns:
                        print("You lost by",cruns-pruns,", better luck next time")
                        losses+=1
            elif toss!=coin:
                print("Darn, you lost the toss")
                choice=r.randint(1,2)
                if choice==1:
                    pruns=0
                    cruns=0
                    print("The computer chose to bat!")
                    i=0
                    while i<overs:
                        print()
                        bat=r.randint(1,6)
                        ball=int(input("How many runs do you think they will go for?"))
                        if bat==ball:
                            print("Well done! opponent is now out")
                            break
                        elif bat!=ball and bat<7:
                            print("So close, your opponent scored",bat,"runs and now they have",cruns+bat,"runs in total")
                            cruns+=bat
                            i+=1
                        elif ball>=7:
                            print("Bad ball :( opponent scored ",bat,"runs and now has",cruns+bat)
                            cruns+=bat
                            i+=1
                    i=0
                    while i<overs:
                        print()
                        bat=int(input("How many runs would you like to go for"))
                        ball=r.randint(1,6)
                        if bat==ball:
                            print("OPPS!, you are out and you scored a total of",pruns)
                            break
                        elif bat!=ball and bat<7:
                            print("Nice shot, you scored",bat,"runs and now have",pruns+bat,"runs in total")
                            pruns+=bat
                            i+=1
                        elif bat>=7:
                            print("You cant score 7 or more runs, try again")
                            i+=1
                        if pruns>cruns:
                            break
                    print()
                    print("In the end you had",pruns,"and the computer had",cruns)
                    if pruns>cruns:
                        print("You won by",pruns-cruns)
                        wins+=1
                    elif cruns>pruns:
                        print("You lost by",cruns-pruns,", better luck next time")
                        losses+=1
                elif choice==2:
                    pruns=0
                    cruns=0
                    print("Computer chose to bowl!")
                    i=0
                    while i<overs:
                        print()
                        bat=int(input("How many runs would you like to go for"))
                        ball=r.randint(1,6)
                        if bat==ball:
                            print("OPPS!, youre out and you scored a total of",pruns)
                            break
                        elif bat!=ball and bat<7:
                            print("Nice shot, you scored",bat,"runs and now have",pruns+bat,"runs in total")
                            pruns+=bat
                        elif bat>=7:
                            print("You cant score 7 or more runs, try again")
                    i=0
                    while i<overs:
                        print()
                        bat=r.randint(1,6)
                        ball=int(input("How many runs do you think they will go for?"))
                        if bat==ball:
                            print("Well done! opponent is now out")
                            break
                        elif bat!=ball and bat<7:
                            print("So close, your opponent scored",bat,"runs and now they have",cruns+bat,"runs in total")
                            cruns+=bat
                        elif ball>=7:
                            print("Bad ball :( opponent scored ",bat,"runs and now has",cruns+bat)
                            cruns+=bat
                        if cruns>pruns:
                            break
                    print()
                    print("In the end you had",pruns,"and the computer had",cruns)
                    if pruns>cruns:
                        print("You won by",pruns-cruns)
                        wins+=1
                    elif cruns>pruns:
                        print("You lost by",cruns-pruns,", better luck next time")
                        losses+=1
            
            
    elif c==2:
        print()
        print("You won",wins," times and lost",losses," time, come again later, enjoy your day!")
        break
    else:
        print()
        print("The chice entered is invalid!")
        print()
