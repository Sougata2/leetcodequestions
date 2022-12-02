def third_largest_element(nums: list):
    k = 3
    nums.sort()
    for i in range(len(nums)-2, -1, -1):
        if k == 1:
            return nums[i+1]
        if nums[i] != nums[i+1]:
            k -= 1
        else:
            continue
    if k == 1:
        return nums[0]
    return nums[len(nums)-1]

print(third_largest_element([3, 2, 1]))
print(third_largest_element([2, 2, 3, 1]))
print(third_largest_element(1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7))
print(third_largest_element([1, 1, 2]))
