def maximum_gap(nums):
    nums.sort()
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i-1])
    return max_gap

if __name__ == "__main__":
    print(maximum_gap([3, 6, 9, 1]))
    print(maximum_gap([10]))