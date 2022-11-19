def searchRotatedArray(nums, target):
    n = len(nums)
    seperation = 0
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            seperation = i
    
    if nums[seperation] <= target <= nums[n-1]:
        return binary_search(nums, target, seperation, n-1)
    
    return binary_search(nums, target, 0, seperation-1)



def binary_search(array, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1
        else:
            return mid
    return -1
    

if __name__ == "__main__":
    print(searchRotatedArray([4, 5, 6, 7, 0, 1, 2], 0))
    print(searchRotatedArray([4, 5, 6, 7, 0, 1, 2], 3))
    print(searchRotatedArray([1], 0))
    
