def two_sum(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        s = nums[left] + nums[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left + 1, right + 1]
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 3, 4], 6))
    print(two_sum([-1, 0], -1))
