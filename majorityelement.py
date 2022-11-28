def majority_element(nums):
    nums.sort()
    limit = len(nums) // 2
    num_count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            num_count += 1
        else:
            if num_count > limit:
                return nums[i-1]
            num_count = 1
    return nums[len(nums)-1] 


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([1]))
