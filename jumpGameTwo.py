# Brute force solution
def jump_game(nums, n, ans, jumps=0, ind=0):
    if ind >= n - 1:
        ans.append(jumps)
        return

    for i in range(1, nums[ind] + 1):
        jump_game(nums, n, ans, jumps + 1, ind + i)


# O(n) solution.
def jump_game_fast(nums: list[int]):
    n = len(nums)
    l = r = 0
    jumps = 0
    while r < n - 1:
        max_jump = 0
        for i in range(l, r+1):
            max_jump = max(max_jump, i + nums[i])

        l = r+1
        r = max_jump
        jumps += 1

    return jumps


nums = [2, 3, 1, 1, 4]
ans = []
n = len(nums)
jump_game(nums, n, ans)
print(min(ans))

print(jump_game_fast(nums))
