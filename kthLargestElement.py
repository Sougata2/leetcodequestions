def kth_largest_element(nums, k):
    nums.sort()
    for i in range(len(nums)-1, -1, -1):
        if k == 1:
            return nums[i]
        k -= 1
    return -1

print(kth_largest_element([3, 2, 1, 5, 6, 4], 2))
print(kth_largest_element([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))