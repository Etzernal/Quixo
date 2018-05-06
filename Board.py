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
	
	
	
	
"""
A class is a way of grouping functions (as methods) and data (as properties) into a logical unit
If you want to regroup functions, just create a module in a new .py file.
class Class:
    def init(self,name,features_of_class):
        self.name = name
        self.features_of_class = features_ofclass #This is a class variable
    def function():
        #this function does something

#This is an object a.k.a subclass
class Object(Class):
    def init(self,name,features_of_class,features_of_object):
        Class.init(self,name,features_of_class)
        self.features_of_object = features_of_object

#These are also objects
Class1 = Class("1") #This is an object of Class. 
Object = Object("1") #This is an object of Object
"""