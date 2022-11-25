def single_number(nums):
    nums.sort()
    num_count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            num_count += 1
        else:
            if num_count == 1:
                return nums[i-1]
            else:
                num_count = 1

    if num_count == 1:
        return nums[len(nums)-1]
    return -1


def single_number_bit_manipulation(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor


if __name__ == "__main__":
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number([2, 2, 1]))
    print(single_number([1]))
    print()
    print(single_number_bit_manipulation([4, 1, 2, 1, 2]))
    print(single_number_bit_manipulation([2, 2, 1]))
    print(single_number_bit_manipulation([1]))
