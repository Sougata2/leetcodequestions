def merge_sorted_arrays(num1, m, num2, n):
    itr1 = m - 1
    itr2 = n - 1
    itr3 = m + n - 1
    while itr2 >= 0:
        # compare the last element. and update the array at the last.
        if itr1 >= 0 and num1[itr1] > num2[itr2]:
            num1[itr3] = num1[itr1]
            itr1 -= 1
        else:
            num1[itr3] = num2[itr2]
            itr2 -= 1
        itr3 -= 1


list1 = [1, 2, 3, 0, 0, 0]
list2 = [2, 5, 6]
merge_sorted_arrays(list1, 3, list2, 3)
print(list1)
