#Prints the board and makes it look pretty
def printBoard(board):	
	print("+" + "---" + "+" + "---" + "+" + "---" + "+")
	print("|" + " " + board[0][0] + " " + "|" + " " + board[0][1] + " " + "|" + " " + board[0][2] + " " + "|")
	print("+" + "---" + "+" + "---" + "+" + "---" + "+")
	print("|" + " " + board[1][0] + " " + "|" + " " + board[1][1] + " " + "|" + " " + board[1][2] + " " + "|")
	print("+" + "---" + "+" + "---" + "+" + "---" + "+")
	print("|" + " " + board[2][0] + " " + "|" + " " + board[2][1] + " " + "|" + " " + board[2][2] + " " + "|")
	print("+" + "---" + "+" + "---" + "+" + "---" + "+")
	
#Getting the user input for a position
def getUserPosition(board, player):
	winningGame = False		
	printBoard(board)
	
	#Runs while the game is not complete
	while not winningGame:
		print("\n" + player + "'s turn!")

		#Get the input and check for validity
		row = int(input("Pick a row (1,2,3): "))
		checkValidInput(row, board, player)
		col = int(input("Pick a column (1,2,3): "))
		checkValidInput(col, board, player)
		
		#Check if the position has been filled
		userPosition = board[row - 1][col - 1]
		checkValidLocation(userPosition, board, player)
		
		#Fills empty spot with X or O
		board[row - 1][col - 1] = player
		
		#Checks if the last move wins
		if isWinner(board, player):	
			printBoard(board)
			print("\n" + player,"Wins!")
			exit()
		
		isBoardFull(board)
			
		if player == "X":
			player = "O"
		else:
			player = "X"	

		printBoard(board)

def isWinner(bo, pl):
	return ((bo[2][0] == pl and bo[2][1] == pl and bo[2][2] == pl) or # across the top
	(bo[1][0] == pl and bo[1][1] == pl and bo[1][2] == pl) or # across the middle
	(bo[0][0] == pl and bo[0][1] == pl and bo[0][2] == pl) or # across the bottom
	(bo[2][0] == pl and bo[1][0] == pl and bo[0][0] == pl) or # down the plft side
	(bo[2][1] == pl and bo[1][1] == pl and bo[0][1] == pl) or # down the middle
	(bo[2][2] == pl and bo[1][2] == pl and bo[0][2] == pl) or # down the right side
	(bo[2][0] == pl and bo[1][1] == pl and bo[0][2] == pl) or # diagonal
	(bo[2][2] == pl and bo[1][1] == pl and bo[0][0] == pl)) # diagonal

#Checks if all the spots in the board have been filled
def isBoardFull(board):
	count = 0
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j] == 'X' or board[i][j] == 'O':
				count += 1
				
	if count == 9:
		printBoard(board)
		print("\nIt's a Tie!")
		exit()
	else:
		pass				
					
#Check if the input is within the list indecies
def checkValidInput(userInput, board, player):
	if userInput > 3 or userInput < 1:
		print("Error: Input out of bounds\n")
		getUserPosition(board, player)
	else:
		pass

#Check if the spot is already in use
def checkValidLocation(position, board, player):
	if position != " ":
		print("Error: Position already taken\n")
		getUserPosition(board, player)
	else:
		pass
	
#Initialize the board list
def initBoard():
	board = [[0 for x in range(3)] for y in range(3)] 
	for i in range(0,3):
		for j in range(0,3):
			board[i][j] = " "
	getUserPosition(board, "X") #Starting player is X
			
def main():
	print("Welcome to Tic Tac Toe\n")
	initBoard()
		
		
if __name__ == "__main__":	
	main()