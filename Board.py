import string
#Initiates board creation
def createboard(size):
	""" creates an empty fresh new board for gameplay where size is the number of rows and columns"""
	board = []
	horizontal = []
	for x in range(size):
		horizontal.append("0")
	for y in range(size):
		board.append([y+1] + horizontal)
	alphabets = list(string.ascii_uppercase)
	board.insert(0,["-"]+ alphabets[:size])
	return board

#to get the currentboard
def get_board(board):
	currentboard = board
	return currentboard
	#Gotta get the current board from move class
	
def display(board):
	for i in board:
		print (i)
