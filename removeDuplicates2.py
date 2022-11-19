def remove_duplicate(nums):
    n = len(nums)
    k = 0
    dupe_count = 0
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            if dupe_count < 1:
                dupe_count += 1
            else:
                continue
        else:
            dupe_count = 0
        nums[k + 1] = nums[i]
        k += 1
    print(nums[:k + 1])
    return k+1


if __name__ == "__main__":
    print(remove_duplicate([1, 1, 1, 2, 2, 3]))
    print(remove_duplicate([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(remove_duplicate([1, 2, 2, 2, 2, 2, 2, 3, 4, 4]))
    print(remove_duplicate([1, 2, 3]))
    print(remove_duplicate([1]))
    print(remove_duplicate([]))
