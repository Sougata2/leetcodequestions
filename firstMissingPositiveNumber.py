def first_missing_positive_number(nums : list[int]):
    # samllest positive missing number must be in [1....n+1] whereas n is length of list.
    n = len(nums)
    hashTable = [0]*(n+1)

    for i in range(n):
        if nums[i] <= 0 or nums[i] >= n+1:  # ignore the values that are greater than equal to n+1 or is 0.
            continue
        hashTable[nums[i]] = 1

    ind = 1
    while ind < n+1 and hashTable[ind] != 0:
        ind += 1

    return ind
    
    

    


    


print(first_missing_positive_number([7,8,9,11,12]))
print(first_missing_positive_number([3, 4, -1, 1]))
print(first_missing_positive_number([1,2,0]))

