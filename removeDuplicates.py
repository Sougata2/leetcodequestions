def remove_duplicates(nums):
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k+1] = nums[i]
            k += 1
    print(nums)
    return k + 1

print(remove_duplicates([1, 1, 1, 2, 2, 3]))
print(remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(remove_duplicates([1, 2, 2, 2, 2, 2, 2, 3, 4, 4]))
print(remove_duplicates([1, 2, 3]))
print(remove_duplicates([1]))
print(remove_duplicates([]))