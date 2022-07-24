def majority_element(nums):
    nums.sort()
    output = None
    limit = len(nums) // 2
    count = 1
    if len(nums) > 1:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
                if count > limit:
                    output = nums[i]
            else:
                count = 1
    else:
        output = nums[0]

    return output


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([1]))
