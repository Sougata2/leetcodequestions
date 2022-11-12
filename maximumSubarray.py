from cmath import inf


def maximum_subarray(nums: list[int]):
    current_sum = 0
    max_sum = -inf
    for i in nums:
        current_sum = max(i, current_sum + i)
        max_sum = max(current_sum, max_sum)

    return max_sum


print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
