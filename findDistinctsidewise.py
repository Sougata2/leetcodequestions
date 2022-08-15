def differences(arr, n):
    ans = []
    def find_distinct(l, r):
        res = 0
        i = l
        while i < r:
            while i < r-1 and arr[i] == arr[i+1]:
                i += 1
            res += 1
            i += 1
        return res

    for i in range(n):
        l = find_distinct(0, i)
        r = find_distinct(i+1, n)
        ans.append(l-r)
    print(ans)


differences([4, 3, 3], 3)
differences([4, 4, 3, 3], 4)
differences([29, 36, 9, 11, 40, 13, 32, 8, 40], 9)
