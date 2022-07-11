def pascal_triangle(rows):
    # Hard coded prior values.
    triangle_rows = [[1]]
    rows -= 1
    if rows == 0:
        return triangle_rows
    triangle_rows.append([1, 1])
    rows -= 1
    if rows == 0:
        return triangle_rows

    while rows > 0:
        last_row = triangle_rows[-1]
        temp_list = [last_row[0]]
        for i in range(len(last_row)):
            if i == len(last_row)-1:
                temp_list.append(last_row[-1])
            else:
                add = last_row[i] + last_row[i+1]
                temp_list.append(add)
        triangle_rows.append(temp_list)
        rows -= 1
    return triangle_rows


print(pascal_triangle(10))
