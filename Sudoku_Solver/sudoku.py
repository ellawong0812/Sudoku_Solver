def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        # Iterate through each cell in the same row
        if board[pos[0]][i] == num and pos[1] != i:
            # If the number already exists in the same row (excluding the current cell), it's invalid
            return False

    # Check column
    for i in range(len(board)):
        # Iterate through each cell in the same column
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            # Iterate through each cell in the 3x3 box
            if board[i][j] == num and (i, j) != pos:
                return False
                
    # If the number is valid in the current position, return True
    return True


def solve(board):
    # Find the next empty cell in the board
    empty = find_empty(board)
    if not empty:
        # if there is no empty box, the sudoko is solved
        return True
    else:
        row, col = empty

    # Try 1-9 to see which numbers suit the empty box
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            # If i suits the empty box, assign to it
            board[row][col] = i

            # Recursive call to solve all other empty boxes
            if solve(board):
                return True

            # If the recursive call doesn't find a solution, it means the assigned number i led to an incorrect solution. In this case, the function backtracks by resetting the cell value to 0 (board[row][col] = 0)
            board[row][col] = 0

    # If no number from 1 to 9 is valid in the current position, backtrack to the previous cell
    return False


# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku board:")
print_board(board)
print("\nSolving...\n")

if solve(board):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")