def differences(arr, n):
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
        arr[i] = find_distinct(0, i) - find_distinct(i+1, n)
    print(arr)


differences([4, 3, 3], 3)
