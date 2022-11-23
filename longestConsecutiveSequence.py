def longest_consequtive(nums):
    if len(nums) == 1:
        return 1
    best_count = 0
    nums.sort()
    i = 0
    while i < len(nums)-1:
        curr_count = 0
        while i < len(nums)-1 and (nums[i+1] == nums[i]+1 or nums[i+1] == nums[i]):
            if nums[i+1] == nums[i]:
                i += 1
                continue
            curr_count += 1
            i += 1
        curr_count += 1
        best_count = max(best_count, curr_count)
        i += 1

    return best_count


if __name__ == "__main__":
    print(longest_consequtive([100, 4, 200, 1, 3, 2]))
    print(longest_consequtive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
