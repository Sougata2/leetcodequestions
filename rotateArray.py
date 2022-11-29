def rotate(nums, k):
    n = len(nums)
    # round k to n if k more than n
    if k > n:
        k %= n
    last_nums = []
    # seperate the last partion and first partion
    # move the first partition to last partition
    for i in range(n-1, -1, -1):
        if i >= n - k:
            last_nums.append(nums[i])
        else:
            nums[i+k] = nums[i]
    
    ind = 0
    for i in range(len(last_nums)-1, -1, -1):
        nums[ind] = last_nums[i]
        ind += 1
    
    print(nums)

rotate([1, 2, 3, 4], 3)
rotate([1, 2], 3)
rotate([0], 1)
    