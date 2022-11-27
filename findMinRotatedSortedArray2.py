def find_min(nums):
    left = 0
    right = len(nums)-1
    ans = nums[0]
    while left <= right:
        if nums[left] < nums[right]:
            ans = min(ans, nums[left])
            break
        
        mid = (left + right) // 2
        ans = min(ans, nums[mid])
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] == nums[right]:
            right -= 1
        else:
            right = mid - 1
        
            
    return ans

if __name__ == "__main__":
    print(find_min([3, 3, 3, 1, 3, 3]))
    print(find_min([2, 2, 2, 0, 1]))
    