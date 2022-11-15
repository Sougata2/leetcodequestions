def set_zero(matrix: list[list]):
    row_indexes = []
    col_indexes = []
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row_indexes.append(i)
                col_indexes.append(j)

    for i in range(n):
        for j in range(m):
            if i in row_indexes:
                matrix[i][j] = 0
            if j in col_indexes:
                matrix[i][j] = 0


def display_matrix(matrix: list[list]):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
    print()


if __name__ == "__main__":
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    display_matrix(grid)
    set_zero(grid)
    display_matrix(grid)

    grid = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    display_matrix(grid)
    set_zero(grid)
    display_matrix(grid)
