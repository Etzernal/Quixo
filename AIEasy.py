import random
#EASY
#picktile
#	create a list with possible tiles to be picked for first turn. aka the border tiles. 
#board = [["-","A","B","C","D"],["1",0,2,2,0],["2",0,2,2,0],["3",2,0,0,2],["4",0,0,0,2]]
#boardsize = len(board[1]) - 1 #4
#playtile = 2
#turncount = 4
tile = []
def AITile(board,boardsize,turncount,playtile):
	#OBTAINING BORDER TILE LIST
	global tile
	directionfrom = "nil"
	tilelist = []
	for i in range(1,boardsize + 1):
		#appending the first and the last row of the board. 
		tilelist.append([1,i])
	for i in range(1,boardsize + 1):
		tilelist.append([boardsize,i])
	for i in range(2,boardsize):
		tilelist.append([i,1])
	for i in range(2,boardsize):
		tilelist.append([i,boardsize])
	#BORDER TILE LIST OBTAINED
	#CHOOSING TILE
	listlength = len(tilelist)-1
	if turncount == 2:
		randomindex = random.randint(1,listlength)
	
	else:
		randomindex = random.randint(1,listlength)
		#checking horizontal 
		coordinates = []
		for row in range(1,boardsize+1): 
			horcount = 0
			for column in range(1,boardsize+1):
				#print(row,column)
				if board[row][column] == playtile:
					horcount += 1
					coordinates.append([row,column])
				else: 
					pass
			#print(coordinates)
			if horcount > 1:
				if board[row][1] == playtile:
					tile = [row,4]
					directionfrom = "left"
					print(tile,directionfrom)
				elif board[row][4] == playtile:
					tile = [row,"1"]
					directionfrom = "right"
					print(tile,directionfrom)
				else: 
					tile = tilelist[randomindex]
					print(tile,directionfrom)
					
		#print(tile,directionfrom)
		for horizontalnum in range(1,boardsize +1):
			vertcount = 0
			for verticalnum in range(1,boardsize +1):				
				#print(verticalnum,board[verticalnum][horizontalnum])	
				if board[verticalnum][horizontalnum] == playtile:
					vertcount += 1
				else:
					pass

			#print(vertcount)
			if vertcount > 1:
				if board[1][horizontalnum] == playtile:
					tile = [4,horizontalnum]
					directionfrom = "above"
					print(tile,directionfrom)
				if board[4][horizontalnum] == playtile:
					tile = [1,horizontalnum]
					directionfrom = "below"
					print(tile,directionfrom)
				else: 
					tile = tilelist[randomindex]
					print(tile,directionfrom)

		print("yay")
		print(tile,directionfrom)
	#TILE CHOSEN	
	return tile,directionfrom
			#look for side tiles occupied then choose side accordingly
				
			#if not just random
	
def randomdirection(tile,directionfrom,board):
	#EDIT TILE DIRECTION
	if directionfrom == "nil":
		[row,column] = tile
		row = int(row)
		column = int(column)
		directionspossible =[]
		#scan which side is the end. allow all other directions
		#check left
		try:
			if board[row][column-1] != "1" and board[row][column-1] != "2" and board[row][column-1] != "0" and board[row][column-1] != "-":
				pass
			else:
				directionspossible.append("left")
			if board[row][column+1] != "1" and board[row][column+1] != "2" and board[row][column+1] != "0" and board[row][column+1] != "-":
				pass
			else:
				directionspossible.append("right")
			if board[row-1][column] != "1" and board[row-1][column] != "2" and board[row-1][column] != "0" and board[row-1][column] != "-":
				pass
			else: 
				directionspossible.append("above")
			if board[row+1][column] != "1" and board[row+1][column] != "2" and board[row+1][column] != "0" and board[row+1][column] != "-":
				pass
			else: 
				directionspossible.append("below")
		except IndexError:
			pass
		#print(len(directionspossible))
		randomdirection = random.randint(0,len(directionspossible)-1)
		directionfrom = directionspossible[randomdirection]
	else:
		pass
	#print(tile,directionfrom)
	#NEW TILE DIRECTION OBTAINED
	return tile,directionfrom

	
def removeAItile(vertical,horizontal,board):
	#need to remove tile --> number to '-' and interact with board object and update board.
	#after Move.removetile() then Board.updateboard()?
	board[int(vertical)][int(horizontal)] = '-'
	return board
		
#tile,directionfrom = AITile(board, boardsize,turncount,playtile)
#tile,directionfrom = randomdirection(tile,directionfrom,board)