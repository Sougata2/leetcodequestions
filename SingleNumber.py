def single_number(nums):
    single_num = None
    nums.sort()
    if len(nums) > 1:
        for i in range(len(nums)):
            if i == 0 or i == len(nums)-1:
                if i == 0:
                    if nums[i] != nums[i+1]:
                        single_num = nums[0]
                        break
                else:
                    if nums[i] != nums[i-1]:
                        single_num = nums[-1]
                        break
            else:
                if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                    single_num = nums[i]
                    break
    else:
        if len(nums) == 0:
            pass
        else:
            single_num = nums[0]
    return single_num


if __name__ == "__main__":
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number([2, 2, 1]))
    print(single_number([1, 2, 3, 4, 5]))
