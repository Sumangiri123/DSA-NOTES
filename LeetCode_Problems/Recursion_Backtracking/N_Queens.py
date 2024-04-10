class Solution(object):
    def solveNQueens(self, n):
        # Helper function to check if it's safe to place a queen at a given position
        def isSafeToPlace(board, row, col, n):
            # Check the row on the left side
            for i in range(col):
                if board[row][i] == 1:
                    return False
            # Check upper diagonal on the left side
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            # Check lower diagonal on the left side
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            return True

        # Helper function to print the board configuration
        def printBoard(board, n):
            board_str = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if board[i][j] == 1:
                        row += "Q"
                    else:
                        row += "."
                board_str.append(row)
            return board_str

        # Initialize the board with all zeros
        board = [[0 for _ in range(n)] for _ in range(n)]
        solutions = []

        # Recursive function to place queens on the board
        def placeQueens(board, col, n):
            # Base case: If all queens are placed, add the board configuration to solutions
            if col == n:
                solutions.append(printBoard(board, n))
                return

            # Try placing a queen in each row of the current column
            for row in range(n):
                if isSafeToPlace(board, row, col, n):
                    board[row][col] = 1 # Place a queen
                    placeQueens(board, col + 1, n) # Recurse to place the next queen
                    board[row][col] = 0 # Undo the move to backtrack

        # Start placing queens from the first column
        placeQueens(board, 0, n)
        return solutions



# Time Complexity

    # The time complexity of the N-Queens problem is O(N!) in the worst-case scenario. This is because, in
    # the worst case, the algorithm explores all possible permutations of placing N queens on an N x N 
    # chessboard. However, the algorithm has several mechanisms to stop exploring a path as soon as a conflict 
    # is detected, which prevents the exploration of all permutations. As a result, the effective time 
    # complexity is generally much less than O(N!). The effective time complexity is determined by the number
    #  of valid placements found, which can be significantly less than the total number of permutations.

# Space Complexity

    # The space complexity of the N-Queens problem is O(N). This is because the algorithm uses a single board
    # of size N x N to represent the chessboard and track the placement of queens. Each cell in the board 
    # can hold a value representing the column index where a queen is placed in that row. The space required
    #  scales linearly with the size of the problem (N), making the space complexity O(N)

# It's important to note that if you choose to store all of the solutions (all valid configurations), the 
# space complexity could increase, depending on the number of valid solutions. However, each solution 
# would still be represented as a list of length N, meaning the space requirement scales linearly with the
# problem size.

# In conclusion, the N-Queens problem showcases the efficiency of the backtracking technique, and while it
# may have a high worst-case time complexity, it effectively handles the search space to find solutions 
# to the problem.