def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens_util(board, 0, n) is False:
        print("No solution exists")
    else:
        print_solution(board)

def solve_n_queens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))


# n = int(input("Enter the size of board"))
n = 8  # Change this to the desired board size
solve_n_queens(n)
