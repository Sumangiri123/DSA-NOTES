def issafetoplace(board,row,col,n):

    # checking left side 
    for i in range(n):
        if board[row][i] == 1:
            return False
        
    # checking upper left diagonal
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    # checking lower left diagonal
    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQ(board,n):
    if not solveNQutil(board,0,n):
        print("Solution doesn't exist")
        return
    
    printBoard(board,n)

def solveNQutil(board,col,n):
    if col >= n:
        return

    