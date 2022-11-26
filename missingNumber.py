def missing_number(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)


print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([3, 0, 1]))
