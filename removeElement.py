def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        nums[k] = nums[i]
        k += 1

    print(nums)
    return k

print(remove_element([3, 2, 2, 3], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))