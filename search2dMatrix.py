def search_2d_matrix(grid, target):
    target_row = grid[0]
    for row in grid:
        if row[0] > target:
            break
        target_row = row

    target_found = binary_search(target_row, target, len(target_row))
    return target_found


def binary_search(nums, x, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if x < nums[mid]:
            high = mid - 1
        elif x > nums[mid]:
            low = mid + 1
        else:
            return True

    return False


if __name__ == "__main__":
    print(search_2d_matrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(search_2d_matrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(binary_search([1], 1, 1))
