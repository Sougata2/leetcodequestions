def min_size_subarray(nums, target):
    min_len = float("inf")
    left = 0
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        while s >= target:
            min_len = min(min_len, i - left + 1)
            s -= nums[left]
            left += 1

    if min_len == float("inf"):
        return 0
    return min_len


print(min_size_subarray([2, 3, 2, 3, 4, 3], 7))
print(min_size_subarray([1, 4, 4], 4))
print(min_size_subarray([1, 1, 1, 1, 1, 1, 1, 1], 11))
print(min_size_subarray([1, 2, 3, 4, 5], 11))
