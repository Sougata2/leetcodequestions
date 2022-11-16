def minimum_path_sum(grid: list[list]):
    ans = []
    n = len(grid)
    m = len(grid[0])
    i = 0
    j = 0
    traverse_matrix(grid, n, m, ans, 0, 0, 0)
    return min(ans)


def traverse_matrix(matrix, n, m, ans, sum, i, j):
    if i >= n or j >= m:
        return

    if i == n-1 and j == m-1:
        sum += matrix[i][j]
        ans.append(sum)

    traverse_matrix(matrix, n, m, ans, sum+matrix[i][j], i+1, j)
    traverse_matrix(matrix, n, m, ans, sum+matrix[i][j], i, j+1)


if __name__ == "__main__":
    matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(minimum_path_sum(matrix))
