def min_in_rotated_sorted_array(nums):
    left = 0
    right = len(nums)-1
    ans = nums[0]
    while left <= right:
        if nums[left] <= nums[right]:
            # array is sorted.
            ans = min(ans, nums[left])
            break

        mid = (left + right) // 2
        ans = min(ans, nums[mid]) # check if the mid index is for minimum value in array.

        # if mid element is greater than the last element then search in right portion
        if nums[mid] >= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

    return ans


print(min_in_rotated_sorted_array([2, 3, 4, 5, 1]))
print(min_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2]))
print(min_in_rotated_sorted_array([11, 13, 15, 17]))
