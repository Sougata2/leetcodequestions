def add_to_array(nums, k):
    carry = 0
    ind = len(nums)-1
    while ind >= 0:
        last_digit = 0

        if k > 0:
            last_digit = k % 10
            k //= 10

        s = nums[ind] + last_digit + carry
        if s > 9:
            nums[ind] = s % 10
            carry = s // 10
        else:
            nums[ind] = s
            carry = 0

        ind -= 1

    # if k is longer than the length of the array.
    if k:
        while k > 0:
            last_digit = k % 10
            k //= 10
            s = last_digit + carry
            if s > 9:
                nums = [s % 10] + nums
                carry = s // 10
            else:
                nums = [s] + nums
                carry = 0

    if carry:
        nums = [carry] + nums

    return nums

print(add_to_array([1, 2, 9, 6], 34))
print(add_to_array([2, 7, 4], 181))
print(add_to_array([2, 1, 5], 806))
print(add_to_array([0], 23))
print(add_to_array([9], 91))
print(add_to_array([6], 809))