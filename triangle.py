# recursive solution.
def minimum_total(triangle: list[list[int]]):
    n = len(triangle)
    ans = []
    traverse_triangle(triangle, n, ans, 0, 0, 0)
    return min(ans)


def traverse_triangle(triangle, n, ans, s, ind, level):
    if level >= n:
        ans.append(s)
        return

    traverse_triangle(triangle, n, ans, s + triangle[level][ind], ind, level + 1)
    traverse_triangle(triangle, n, ans, s + triangle[level][ind], ind + 1, level + 1)


print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimum_total([[-10]]))
