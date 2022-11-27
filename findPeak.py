def find_peak(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums)-1 or nums[mid+1] < nums[mid]):
            return mid
        elif nums[mid + 1] > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print(find_peak([1, 2, 3, 1]))
    print(find_peak([1, 2, 1, 3, 5, 6, 4]))
    print(find_peak([1, 2]))
