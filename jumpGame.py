def jump_game(nums: list[int]):
    l = r = 0
    n = len(nums)
    while r < n-1:
        farthest_jump = 0
        for i in range(l, r+1):
            farthest_jump = max(farthest_jump, i + nums[i])
        
        if nums[farthest_jump] == 0:
            return False
        i = r + 1
        r = farthest_jump
    return True

    


print(jump_game([2, 3, 1, 1, 4]))
print(jump_game([3, 2, 1, 0, 4]))
print(jump_game([0]))
