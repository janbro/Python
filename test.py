boardLen = 100
k = 2
start = [1,1]
target = [2,2]
board = [[-1 for x in range(boardLen)] for x in range(boardLen)] 
turn = 0
board[start[0]-1][start[1]-1]=0
while(board[target[0]-1][target[1]-1]==-1):
	for i in xrange(len(board)):
		for j in xrange(len(board[0])):
			if(board[i][j]==turn):
				for x in xrange(1,k+1):
					try:
						if board[i-x][j] == -1 and i-x>=0:
							board[i-x][j] = turn+1
					except:
						pass
					try:
						if board[i+x][j] == -1 and i+x<boardLen:
							board[i+x][j] = turn+1
					except:
						pass
					try:
						if board[i][j+x] == -1 and j+x<boardLen:
							board[i][j+x] = turn+1
					except:
						pass
					try:
						if board[i][j-x] == -1 and j-x>=0:
							board[i][j-x] = turn+1
					except:
						pass
				try:
					if board[i+2][j+1] == -1 and j+1<boardLen and i+2<boardLen:
							board[i+2][j+1] = turn+1
				except:
					pass
				try:
					if board[i+1][j+2] == -1 and j+2<boardLen and i+1<boardLen:
							board[i+1][j+2] = turn+1
				except:
					pass
				try:
					if board[i-2][j-1]== -1 and j-1>=0 and i-2>=0:
							board[i-2][j-1] = turn+1
				except:
					pass
				try:
					if board[i-1][j-2] == -1 and j-2>=0 and i-1>=0:
							board[i-1][j-2] = turn+1
				except:
					pass
				try:
					if board[i+2][j-1] == -1 and j-1>=0 and i+2<boardLen:
							board[i+2][j-1] = turn+1
				except:
					pass
				try:
					if board[i+1][j-2] == -1 and j-2>=0 and i+1<boardLen:
							board[i+1][j-2] = turn+1
				except:
					pass
				try:
					if board[i-2][j+1] == -1 and j+1<boardLen and i-2>=0:
							board[i-2][j+1] = turn+1
				except:
					pass
				try:
					if board[i-1][j+2] == -1 and j+2<boardLen and i-1>=0:
							board[i-1][j+2] = turn+1
				except:
					pass
	#print "-----------------------"
	#print str(board)[2:-2].replace("],","\n").replace(" [","")
	#print "-----------------------"
	turn+=1
print board[target[0]-1][target[1]-1]