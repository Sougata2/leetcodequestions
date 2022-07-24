def findPath(grid):
    ans = []
    temp = []
    row, col = len(grid), len(grid[0])
    calcPath(row, col, 0, 0, ans, temp, grid)
    return ans

def calcPath(row, col, i, j, ans, temp, grid):
    if i >= row or j >= col:
        return

    temp.append(grid[i][j])

    if i == row-1 and j == col-1:
        ans.append(temp[:])

    calcPath(row, col, i+1, j, ans, temp, grid)
    calcPath(row, col, i, j+1, ans, temp, grid)

    temp.pop()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(findPath(matrix))
