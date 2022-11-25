def single_number(nums: list[int]):
    nums.sort()
    num_count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            num_count += 1
        else:
            if num_count == 1:
                return nums[i-1]
            else:
                num_count = 1
    if num_count == 1:
        return nums[len(nums)-1]
    return -1


print(single_number([2, 2, 3, 2]))
print(single_number([0, 1, 0, 1, 0, 1, 99]))
