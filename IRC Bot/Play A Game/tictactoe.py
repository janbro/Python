import sys

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
finished = 0

def printBoard():
    for x in xrange(0,3):
        for y in xrange(0,3):
            if y<2:
                sys.stdout.write(board[x][y]+"|")
            else:
                sys.stdout.write(board[x][y])
        if x<2:
            print "\n-----"


def checkBoard():
    X = 0
    O = 0
    for x in xrange(0,3):
        if board[x][x] == "X":
            X+=1
        if board[x][x] == "O":
            O+=1
    if X == 3:
            print "You win!"
            return 1
    elif O == 3:
            print "You lost!"
            return -1
    
    X = 0
    O = 0
    
    for x in xrange(0,3):
        if board[x][2-x] == "X":
            X+=1
        if board[x][2-x] == "O":
            O+=1
    if X == 3:
        print "You win!"
        return 1
    elif O == 3:
        print "You lost!"
        return -1
           
    for x in xrange(0,3):
        X = 0
        O = 0 
        for y in xrange(0,3):
            if board[x][y] == "X":
                X+=1
            if board[x][y] == "O":
                O+=1
        if X == 3:
            print "You win!!"
            return 1
        elif O == 3:
            print "You lost!!"
            return -1

    
    for y in xrange(0,3):
        X = 0
        O = 0
        for x in xrange(0,3):
            if board[x][y] == "X":
                X+=1
            if board[x][y] == "O":
                O+=1
        if X == 3:
            print "You win!!!"
            return 1
        elif O == 3:
            print "You lost!!!"
            return -1
    return 0

def makeMove():
    moveBoard = [[0,0,0],[0,0,0],[0,0,0]]
    
    for x in xrange(0,3):
        for y in xrange(0,3):
            print(x),
            print(","),
            print y
            if board[x][y] is not " ":
                moveBoard[x][y] = -1
            else:
                if x == y:
                    temp = 0
                    for q in xrange(0,3):
                        if board[q][q] == "X":
                            temp+=1
                        elif board[q][q] == "O":
                            temp-=.5
                    moveBoard[x][y] += (temp+(abs(temp)-1)*2)
                if (x == 0 and y==2) or (x==2 and y==0):
                    temp = 0
                    for q in xrange(0,3):
                        if board[q][2-q] == "X":
                            temp+=1
                        elif board[q][2-q] == "O":
                            temp-=.5
                    print temp
                    moveBoard[x][y] += (temp+(abs(temp)-1)*2)
                temp = 0
                for p in range(0,3):
                    if board[p][y] == "X":
                        temp+=1
                    elif board[p][y] == "O":
                        temp-=.5
                moveBoard[x][y] += (temp+(abs(temp)-1)*2)
                temp = 0
                for p in range(0,3):
                    if board[x][p] == "X":
                        temp+=1
                    elif board[x][p] == "O":
                        temp-=.5
                moveBoard[x][y] += (temp+(abs(temp)-1)*2)
                
    high = [0,0]
    highestVal = -9
    for x in xrange(0,3):
        for y in xrange(0,3):
            print(moveBoard[x][y]),
            if moveBoard[x][y] > highestVal:
                high = [x,y]
                highestVal = moveBoard[x][y]
        print ""
    board[high[0]][high[1]] = "O"

while finished == 0:
    inp = input("\nMove(#,#)?:")
    pos = inp.split(",")
    xcoord = int(pos[0])-1
    ycoord = int(pos[1])-1
    board[xcoord][ycoord] = "X"
    makeMove()
    printBoard()
    finished = checkBoard()
