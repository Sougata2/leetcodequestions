def max_product(nums: list):
    max_prod = min_prod = ans = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            min_prod, max_prod = max_prod, min_prod
        max_prod =  max(max_prod * nums[i], nums[i])
        min_prod =  min(min_prod * nums[i], nums[i])
        ans = max(ans, max_prod)
    
    return ans

print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))
print(max_product([2, -5, -2, -4, 3]))
