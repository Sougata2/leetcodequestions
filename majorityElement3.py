def majority_element(nums):
    nums.sort()
    num_count = 1
    ans = []
    limit = len(nums) // 3
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            num_count += 1
        else:
            if num_count > limit:
                ans.append(nums[i-1])
            num_count = 1

    if num_count > limit:
        ans.append(nums[len(nums)-1])
    return ans


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([1]))
    print(majority_element([1, 2]))
