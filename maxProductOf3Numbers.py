def max_product(nums: list):
    nums.sort()
    third = nums[len(nums)-1]
    first = nums[0]
    second = nums[1]
    ans = first * second * third
    for i in range(1, len(nums)-2):
        first = nums[i]
        second = nums[i+1]
        ans = max(ans, first * second * third)

    return ans


print(max_product([-1, -2, -3, -4]))
print(max_product([1, 2, 3]))
print(max_product([1, 2, 3, 4]))
print(max_product([-1, -2, -3]))