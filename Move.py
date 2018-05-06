"""
Type of moves taken by each player e.g. Checktile, Removetile, Placetile, Checkwin
Move will recieve data from board to get moves from player and pass it to tile for changing value. then move
will recieve data from tile to change board before returning board value to the currentboard class. 
"""
import string
alphabets = list(string.ascii_uppercase)
turncount = 0
#Obtain board from CurrentBoard, after player selects tile, tile data is sent to tile class. tile data recieved from tile. board is updated. Board data sent from removetile to currentboard.
#Tile is selected by player.
def picktile():
	choosetile = input("Please pick a tile to remove. E.g. A1,A2,B1,B2... etc >")
	return choosetile
#Tile is checked by computer to see if valid move, need to check if the tile are at the borders... 
def checktile(choosetile,playernumber,board):
	#need to find the corresponding tile with the position of tile given by the player. 
	#allow if tile = 0 or correct tile number. return true
	#if not return false
	tileposition = list(choosetile)
	#print(tileposition)
	horizontalvalue = alphabets.index(tileposition[0]) + 1
	verticalvalue = int(tileposition[1])
	#print (horizontalvalue)
	#print (verticalvalue)
	tilevalue = board[verticalvalue][horizontalvalue]
	#print(tilevalue)
	#need to check which player it is 1 or 2
	#i.e. if tilevalue == '0' or str(playernumber):
	#     	return True, verticalvalue, horizontalvalue 
	#     else: 
	#     	return False
	if playernumber%2 == 1:
		playtile = "1"
	elif playernumber%2 == 0:
		playtile = "2"
	if (tilevalue == "0") or (tilevalue == playtile):
		#for the tiles in the middle validtile = False
		validtile = True
		for hor in range(2,len(board[1])-1):
			#print(hor)
			for vert in range(2,len(board[1])-1):
				#print(vert)
				if (vert == verticalvalue) and (hor == horizontalvalue):
					#print(vert,hor,verticalvalue,horizontalvalue)
					validtile = False
					#print(validtile)
	else:
		validtile = False
	return verticalvalue,horizontalvalue,validtile,playtile
#Tile is removed if checktile returns true
def removetile(validtile,vertical,horizontal,board):
	#need to remove tile --> number to '-' and interact with board object and update board.
	#after Move.removetile() then Board.updateboard()?
	if validtile == True:
		#replace tile with '-'	
		board[vertical][horizontal] = '-'
		#update board after this** - call the board function?
	elif validtile == False:
		print ("You cannot remove this tile")	
	currentboard = board 
	return currentboard
#Obtain board from CurrentBoard, after player places tile, board is updated. Board data sent from placetile to currentboard
#def placetile():
	#need to select direction to put in the tile from
	#check if can put tile in that position if not reject
#def checkwin():
	#check for tiles in a row.
	#if win then end the game and show who is the winner. 
def checkturn(nameofplayers,turncount):
	#check for number of turns
	turncount += 1
	#check whose turn
	playernumber = turncount%len(nameofplayers) 
	playerturn = nameofplayers[playernumber - 1]
	return turncount,playerturn,playernumber
def checkdirection(verticalvalue,horizontalvalue,board):
	#get input from player to see which direction player wants to input from
	#check if direction is valid. 
	#by looking at the tile before '-'
	placecheck = False
	while placecheck == False:
		insertdirection = int(input("Which direction would you like to insert this tile from? 1)Left,2)Right,3)Up or 4)Below?>"))
		try:
			if insertdirection == 1: #if left, check left of '-' 
				if (board[verticalvalue][horizontalvalue-1] == "0") or (board[verticalvalue][horizontalvalue-1] == "1") or (board[verticalvalue][horizontalvalue-1] == "2") or (board[verticalvalue][horizontalvalue-1] == "-"):
					placecheck = True
				else:
					placecheck = False
			elif insertdirection == 2: #if right, check right of '-'
				if (board[verticalvalue][horizontalvalue+1] == "0") or (board[verticalvalue][horizontalvalue+1] == "1") or (board[verticalvalue][horizontalvalue+1] == "2") or (board[verticalvalue][horizontalvalue+1] == "-"):
					placecheck = True
				else:
					placecheck = False
			elif insertdirection == 3: #if up, check up of '-'
				if (board[verticalvalue-1][horizontalvalue] == "0") or (board[verticalvalue-1][horizontalvalue] == "1") or (board[verticalvalue-1][horizontalvalue] == "2") or (board[verticalvalue-1][horizontalvalue] == "-"):
					placecheck = True
				else:
					placecheck = False
			elif insertdirection == 4: #if down, check down of '-'
				if (board[verticalvalue+1][horizontalvalue] == "0") or (board[verticalvalue+1][horizontalvalue] == "1") or (board[verticalvalue+1][horizontalvalue] == "2") or (board[verticalvalue+1][horizontalvalue] == "-"):
					placecheck = True
				else:
					placecheck = False
		except IndexError:
			placecheck = False
	print(placecheck)
	return insertdirection
def placetile(verticalvalue,horizontalvalue,board,insertdirection,playernumber,playtile):
	verticalvalue = int(verticalvalue)
	horizontalvalue = int(horizontalvalue)
	endboard = len(board[1]) - 1
	#if it is the four corner tiles aka (1,1),(1,n),(n,1)(n,n), only can insert from two directions
	#if it is the other border tiles, can insert only from three directions.
	if insertdirection == 1: #Left means must keep the verticalvalue, horizontal value decreases as it iterates
		newhorizontal = 1
		#get the position of '-' in the board
		#shift from before the position of '-' towards '-',meaning '-' will take value of previous 
		while int(horizontalvalue) > 1:
			board[verticalvalue][horizontalvalue] = board[verticalvalue][horizontalvalue-1]
			horizontalvalue -= 1
		board[verticalvalue][newhorizontal] = playtile
		#tile. And afterwards new tile will be inserted into '-'
		#need to push the remaining tiles
		#need to put tile in that position
	elif insertdirection == 2: #Right means must keep the verticalvalue, horizontal value increases as it iterates
		newhorizontal = endboard
		while int(horizontalvalue) < endboard:
			board[verticalvalue][horizontalvalue] = board[verticalvalue][horizontalvalue+1]
			horizontalvalue += 1
		board[verticalvalue][newhorizontal] = playtile


	elif insertdirection == 3: #Up means must keep the horizontalvalue, vertical value decreases as it iterates
		newvertical = 1
		while verticalvalue > 1:
			board[verticalvalue][horizontalvalue] = board[verticalvalue-1][horizontalvalue]
			verticalvalue -= 1
		board[newvertical][horizontalvalue] = playtile

	elif insertdirection == 4: #Down means must keep the horizontalvalue , vertical value increases as it iterates 
		newvertical = endboard
		while verticalvalue < endboard:
			board[verticalvalue][horizontalvalue] = board[verticalvalue+1][horizontalvalue]
			verticalvalue += 1
	#	board[1][3] = board[2][3]
	#	board[2][3] = board[3][3]
		board[newvertical][horizontalvalue] = playtile
	return board
def checkwin(board):
	boardsize = len(board[1]) - 1
	win = False
	#checking horizontal 
	for rows in board: 
		count1 = 0 
		count2 = 0
		for values in rows:
			if values == "1":
				count1 += 1
			if values == "2":
				count2 += 1
			else: 
				pass
		#print (count1,count2,boardsize)
		if count1 == boardsize:
			print("Player 1 wins!")
			win = True
		elif count2 == boardsize:
			print("Player 2 wins!")
			win = True
	#checking vertical 
	for horizontalnum in range(1,boardsize +1):
		#print (horizontalnum)
		count1 = 0
		count2 = 0
		for verticalnum in range(1,boardsize +1):
			#print(verticalnum,board[verticalnum][horizontalnum])	
			if board[verticalnum][horizontalnum] == "1":
				count1 += 1
			elif board[verticalnum][horizontalnum] == "2":
				count2 += 1
			else:
				pass
		#print (count1,count2)
		if count1 == boardsize:
			print("Player 1 wins!")
			win = True
		elif count2 == boardsize:
			print("Player 2 wins!")
			win = True
	#checking diagonal increment
	countone = 0
	counttwo = 0
	for num in range(1,boardsize +1):
		if board[num][num] == "1":
			countone += 1
		elif board[num][num] == "2":
			counttwo += 1
		else:
			pass
	#print (countone,counttwo)
	if countone == boardsize:
		print("Player 1 wins!")
		win = True
	elif counttwo == boardsize:
		print("Player 2 wins!")
		win = True
	#checking diagonal one decreases
	count3 = 0
	count4 = 0
	horlist = [0]
	for i in range(boardsize,0,-1):
		horlist.append(i)
	#print (horlist)
	for vert in range(1,boardsize +1):
		#print(vert)
		if board[vert][horlist[vert]] == "1":
			count3 += 1
		if board[vert][horlist[vert]] == "2":
			count4 += 1
		else: 
			pass
	#print (count3, count4)
	if count3 == boardsize:
		print("Player 1 wins!")
		win = True
	elif count4 == boardsize:
		print("Player 2 wins!")
		win = True
	return win