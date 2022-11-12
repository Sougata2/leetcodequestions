def rotate_image(matrix: list[list]):
    # transpose the matrix 
    # reverse the rows
    n = len(matrix)

    # TRANSPOSE
    for i in range(n):
        for j in range(n):
            if i - j < 0:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                    
    # REVERSE ROWS
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    

if __name__ == "__main__":
    mtrx = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]
    n = len(mtrx)
    rotate_image(mtrx)
    
    for row in mtrx:
        for num in row:
            print(num, end="  ")
        print()

    