def plus_one(nums: list[int]):
    n = len(nums)

    if nums[-1] + 1 <= 9:
        # if the last digit does not add up to 10
        # then only add one to the last
        nums[-1] += 1
    else:
        carry = 1
        i = n-1
        # starting from the last
        # iterate while carry is not zero
        while carry:
            if i < 0:
                # full array is iterated and still carry if left
                # then insert the carry at the begining.
                # and break out of the loop
                nums.insert(0, carry)
                break

            if nums[i] + carry > 9:
                # if the current digit adds ups to 10
                # take the division by 10 of the addition as carry
                # update the current digit with the remainder of (current digit + carry)
                carry = (nums[i]+carry) // 10
                nums[i] = (nums[i] + carry) % 10

            else:
                # if the current digit does not adds upto 10
                # simply add the carry to the current digit and make the carry zero to close the loop.
                nums[i] += carry
                carry = 0
            i -= 1

    return nums


print(plus_one([2, 1, 9]))
print(plus_one([9, 9, 9, 9]))
