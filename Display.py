import AIEasy
import random

def instructions():
	text="""
Welcome to Quixo. 
How to navigate:
- Just type in the corresponding answer to the question when prompted to.
Gameplay of Quixo:
There are three different difficulties of the Computer in this game - Easy, Medium and Hard. You can choose to play with the computer or
even with your friends. In Quixo, each person is allocated a tile - usually X and Os, which are replaced by '1' and '2' in this game. '0' 
represents an empty tile. To start, a player picks a tile to remove - either a '0' tile or his own number. The player then chooses where 
and in which direction to "push" the tile to the desired position. 
Rules in Quixo:
- Players can only remove tiles which are on the outer side of the baord. 
- Players can only remove tiles which are their own or an empty tile. 
- Players cannot place the tile back in the same spot. 
How to win:
- A player wins by getting n number of tiles in a row/column/diagonally where n is the width of the board determined by the player.
		"""
	print(text)
def numberofplayers():
	boardsize = int(input("What will the board size be? Please input a number. >"))
	playersnumber = int(input("How many players will there be?(Pick a number from 2-4)>"))
	humanplayer = int(input("How many human players will there be? Note: There can only be one computer player in each game>"))
	nameofplayers = []
	counter = 1
	for x in range(humanplayer):
		playername = input("Please input player "+str(counter)+"'s name.>")
		nameofplayers.append(playername)
		counter += 1
	if playersnumber - humanplayer == 1:
		nameofplayers.append("Computer")
		difficulty = input("Please select the difficulty level for the computer: Easy, Medium or Hard>")
	else:
		difficulty = 0
	valueslist = [playersnumber,humanplayer,nameofplayers,difficulty,boardsize]
	return valueslist
tile = []
def AIEasyTurn(currentboard,boardsize,turncount):
	global tile
	Board.display(currentboard)
	turncount,playerturn,playernumber = Move.checkturn(nameofplayers,turncount)
	if playernumber%2 == 1:
		playtile = "1"
	elif playernumber%2 == 0:
		playtile = "2"
	print("Turn: " + str(turncount))
	print("It is " + str(playerturn) + "'s turn now!")
	tile,directionfrom = AIEasy.AITile(currentboard, boardsize,turncount,playtile)
	print(tile,directionfrom)
	tile,directionfrom = AIEasy.randomdirection(tile,directionfrom,currentboard)
	[verticalvalue,horizontalvalue] = tile
	validtile = True
	"""tile is removed, value changed to '-'"""
	currentboard = AIEasy.removeAItile(verticalvalue,horizontalvalue,currentboard)
	"""Displays board after tile is removed.""" 
	Board.display(currentboard)
	if directionfrom == "left":
		directionfrom = 1
	elif directionfrom == "right":
		directionfrom = 2
	elif directionfrom == "above":
		directionfrom = 3
	elif directionfrom == "below":
		directionfrom = 4
	"""Place tile on board"""
	currentboard = Move.placetile(verticalvalue,horizontalvalue,currentboard,directionfrom,playernumber,playtile)
	"""Display the new board"""
	
	Board.display(currentboard)
	"""Check for win condition"""
	win = Move.checkwin(currentboard)
	#END OF TURN
	return win,currentboard,turncount

	
################################################################################################################
#stuff to import
import Board
import Move
#variables to set
turncount = 0
#stuff to execute
"""This prints out the starting text/welcoming message"""
instructions()
"""This assigns the values to variables to access later on"""
#[playersnumber,humanplayer,nameofplayers,difficulty,boardsize] = numberofplayers()
boardsize, playersnumber, humanplayer, nameofplayers, difficulty = 4,2,1,["J","Computer"],"<insertdifficulty>" 

"""This creates a newboard"""
newboard = Board.createboard(boardsize)
"""Check turn number and whose turn"""
currentboard = newboard

def moveturn(currentboard,turncount):
	#START OF TURN
	"""This displays the board in a better format"""
	Board.display(currentboard)
	turncount,playerturn,playernumber = Move.checkturn(nameofplayers,turncount)
	print("Turn: " + str(turncount))
	print("It is " + str(playerturn) + "'s turn now!")
	"""This prompts guy to select the tile to remove"""
	tiletoremove = Move.picktile() #tile position
	"""This checks if the tile that the guy selects is a valid move and returns true or false"""
	verticalvalue,horizontalvalue,validtile,playtile = Move.checktile(tiletoremove,playernumber,currentboard) #True/False
	"""tile is removed, value changed to '-'"""
	currentboard = Move.removetile(validtile,verticalvalue,horizontalvalue,currentboard)
	"""Displays board after tile is removed.""" 
	Board.display(currentboard)
	"""Check direction chosen by player to see if valid or not. """
	insertdirection = Move.checkdirection(verticalvalue,horizontalvalue,currentboard)
	"""if placecheck is true, start placing tiles onto the board"""
	currentboard = Move.placetile(verticalvalue,horizontalvalue,currentboard,insertdirection,playernumber,playtile)
	"""Display the new board"""
	Board.display(currentboard)
	"""Check for win condition"""
	win = Move.checkwin(currentboard)
	#END OF TURN
	return win,currentboard,turncount

if int(playersnumber) - int(humanplayer) == 1:
	win,currentboard,turncount = moveturn(currentboard,turncount)
	while win == False:
		win,currentboard,turncount = AIEasyTurn(currentboard,boardsize,turncount)
		print(win,currentboard,turncount)
		win,currentboard,turncount = moveturn(currentboard, turncount)
		print(win,currentboard,turncount)
else:
	win,currentboard,turncount = moveturn(currentboard,turncount)	
	while win == False:
		win,currentboard,turncount = moveturn(currentboard,turncount)
