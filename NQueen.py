# N QUEEN RECURSIVE SOLUTION
def n_queen_problem(n):
    ans = []
    board = [["."]*n]*n
    traverse(board, n, ans, 0)
    return ans


def traverse(board, n, ans, col):
    if col == n:
        ans.append(board.copy())
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            traverse(board, n, ans, col+1)
            board[row][col] = "."


def is_safe(board, row, col, n):
    row_cpy = row
    col_cpy = col

    # upper diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    row = row_cpy
    col = col_cpy
    # row
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1


    col = col_cpy
    # lower digonal
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False

        row += 1
        col -= 1

    return True

print(n_queen_problem(3))
