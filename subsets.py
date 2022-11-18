def subsets(nums, n, ans, temp, ind):
    if ind >= n:
        ans.append(temp[:])
        return
    
    temp.append(nums[ind])
    subsets(nums, n, ans, temp, ind + 1)
    temp.pop()
    subsets(nums, n, ans, temp, ind + 1)

def subsets_two(nums, n, ans, temp, ind):
    ans.append(temp[:])
    for i in range(ind, n):
        temp.append(nums[i])
        subsets(nums, n, ans, temp, i+1)
        temp.pop()
    
if __name__ == "__main__":
    arr = [1, 2, 3]
    ans = []
    n = len(arr)
    temp = []
    subsets(arr, n, ans, temp, 0)
    print(ans)

    ans.clear()
    temp.clear()
    subsets_two(arr, n, ans, temp, 0)
    print(ans)
