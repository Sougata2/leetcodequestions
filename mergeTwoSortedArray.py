def merge_sorted_array(nums1, nums2, m, n):
    size = n + m
    first = second = third = 0
    merged_array = []
    while third < size and first < m and second < n:
        if nums1[first] < nums2[second]:
            merged_array.append(nums1[first])
            first += 1
            if first >= m:
                for i in range(second, n):
                    merged_array.append(nums2[i])
        else:
            merged_array.append(nums2[second])
            second += 1
            if second >= n:
                for i in range(first, m):
                    merged_array.append(nums1[i])

    return merged_array


def merge_sorted_array_inplace(nums1, nums2, m, n):
    # iterate reversly and place the largest of the two array at last.

    i, j = m - 1, n - 1
    for right in range(m+n-1, -1, -1):
        if j < 0:
            break
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[right] = nums1[i]
            i -= 1
        else:
            nums1[right] = nums2[j]
            j -= 1

arr = [1, 2, 3, 0, 0, 0]
# arr = [1]
# arr = [0]
arr2 = [2, 5, 6]
# arr2 = []
# arr2 = [1]
# shift_right(arr, 5)
# print(arr)
# print(merge_sorted_array([1, 2, 3, 7], [2, 5, 6], 4, 3))
merge_sorted_array_inplace(arr, arr2, 3, 3)
print(arr)
