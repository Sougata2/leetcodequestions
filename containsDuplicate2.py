def contains_duplicate(nums, k):
    map = {}
    for i in range(len(nums)):
        if map.get(nums[i], None) is None:
            map[nums[i]] = i
        else:
            if abs(map[nums[i]] - i) <= k:
                return True
            else:
                map[nums[i]] = i
    return False

print(contains_duplicate([1, 2, 3, 1], 3))
print(contains_duplicate([1, 0, 1, 1], 1))
print(contains_duplicate([1, 2, 3, 1, 2, 3], 2))
print(contains_duplicate([4, 1, 2, 3, 1, 5], 3))

