def issafetoplace(board, row, col, n):
    # Checking left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Checking upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checking lower left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQutil(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if issafetoplace(board, row, col, n):
            board[row][col] = 1 # Place a queen at the current position

            if solveNQutil(board, col + 1, n):
                return True

            board[row][col] = 0 # Backtrack if no solution is found

    return False

def solveNQ(board, n):
    if not solveNQutil(board, 0, n):
        print("Solution doesn't exist")
        return

    printBoard(board, n)

def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end="")
            else:
                print(".", end="")
        print()

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

solveNQ(board, 4)


# Time Complexity :
# Space Complexity :
    