def matrix_path(matrix):
    s = 0
    i, j = 0, 0
    n = len(matrix) - 1
    while True:
        curr = matrix[i][j]
        down = matrix[i + 1][j]
        right = matrix[i][j + 1]
        s += curr
        if down and right:
            if down > right:
                # go down
                i += 1
            elif down < right:
                # go right
                j += 1
            else:
                # go down
                i += 1
            s += curr
        else:
            if not down:
                # go right
                j += 1
            elif not right:
                # go down
                i += 1
            s += curr

        if i == n and j == n:
            break


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix_path(matrix))
