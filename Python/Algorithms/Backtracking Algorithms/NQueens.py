global N,k
k=0
N=int(input("Enter board size: "))
def printSolution(board):
	for i in range(N): 
		for j in range(N): 
			print ("Q" if board[i][j]==1 else "-", end=' ')
		print()
def isSafe(board, row, col):  
	for i in range(col):  #checking if pos already occupied
		if board[row][i] == 1: 
			return False
  #upper diagonal left side
	for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
		if board[i][j] == 1: 
			return False
	#lower diagonal left side 
	for i,j in zip(range(row,N,1), range(col,-1,-1)): 
		if board[i][j] == 1: 
			return False
	return True
def PlaceQueens(board, col):
  global k
  if col == N:
    print('Solution ',k+1,':\n')
    k=k+1
    printSolution(board)
    return True
  for i in range(N): 
    res=False
    if isSafe(board, i, col): 
      board[i][col] = 1
      res = PlaceQueens(board, col + 1) or res
      board[i][col] = 0
  return res
def NQueens(): 
  board = [[0 for i in range(N)] for i in range(N)]
  if PlaceQueens(board, 0) == False and k==0: 
    print("Solution does not exist")
    return False 
  return True
NQueens() 

