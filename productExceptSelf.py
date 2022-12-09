def product_except_self(nums):
    n = len(nums)
    right = [1]*n
    left = [1]*n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    for i in range(n):
        nums[i] = left[i]*right[i]

    # print(nums, left, right)
    return nums


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
