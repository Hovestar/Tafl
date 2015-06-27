""" This is a practive pretty printing of the board for when we don't have graphics, will be replaced with c++"""

def PrintPretty(board):
	""" Board is a 9x9 list of 0,1,2,3s."""
	string = '+'
	for j in range(9):
		for _ in range(9):
			string += '-+'
		string +='\n|'
		for i in range(9):
			if board[j][i] == 0:
				string += ' |'
			elif board[j][i] == 1:
				string += 'M|'
			elif board[j][i] == 2:
				string += 'S|'
			elif board[j][i] == 3:
				string += 'K|'
			else: 
				print('Something is wrong!')
		string += '\n'
	string += '+'
	for i in range(9):
		string += '-+'
	print(string)


PrintPretty([[(i+j)%4 for i in range(9)] for j in range(9)]) #Just a test
