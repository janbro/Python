print "The object of the game is to make your opponent pick the last coin.\nOn each turn you can take 1,2, or 3 coins. The game starts with 18 coins."
coins = 18
nimsum = 4 #Nimsum is precalculate based on array of the options, k, of length n, where k is an array of consecutive positive integer, Nimsum = k[0]+k[n]
take = 0
won = False
while coins > 0:
    inp = 0
    print "How many coins would you like to remove?"
    ###Annoying input filtering
    while inp<1 or inp>3:
        inp = raw_input()
        try:
            inp = eval(inp)
        except:
            print "Bad input!"
            continue
        if inp<1 or inp>3:
            print "Bad input"
    ###End of annoying input filtering
    coins-=inp
    print "Coins left: %i" % (coins,)
    if coins <= 0:
        print "You Lose!!!"
        break
    nimmultiple = 1
    while nimsum*nimmultiple<coins: #Calculate the nimNumber, the (largest multiple of the nimsum)+1 which is less than coins
        nimmultiple+=1
    nimmultiple-=1
    nimnumber=nimsum*nimmultiple+1
    if won: #Finish nimpairs all the way home, we've won!
        take = nimsum-inp
    elif coins == nimnumber: #We're screwed
        take = 1
    elif not won: #Get to nimnumber. We've won at this point
        take = coins-nimnumber
        won = True
    print "The computer took %i coins" % (take,)
    coins-=take
    print "Coins left: %i" % (coins,)
    if coins <= 0:
        print "You win!!!"
        break
    
