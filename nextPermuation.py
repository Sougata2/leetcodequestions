def next_permute(nums):
    # find the first non decreasing increasing number
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i > 0:
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[j], nums[i-1] = nums[i-1], nums[j]
    nums[i:] = nums[i:][::-1]




if __name__ == "__main__":
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    # nums = [5, 4, 3, 2, 1]
    # nums = [1, 3, 2]
    next_permute(nums)
    print(nums)
