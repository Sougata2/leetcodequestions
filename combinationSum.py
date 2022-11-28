def combination_sum(nums, target):
    ans = []
    temp = []
    n = len(nums)
    traverse(nums, ans, temp, n, target, 0)
    return ans

def traverse(nums, ans, temp, n, target, ind):
    if target <= 0:
        if target == 0:
            ans.append(temp[:])
        return
    
    for i in range(ind, n):
        temp.append(nums[i])
        traverse(nums, ans, temp, n, target-nums[i], i)
        temp.pop()

if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
    print(combination_sum([2, 3, 5], 8))