def distinct(arr):
    n = len(arr)
    i = 0
    ans = 0
    while i < n:
        while i < n-1 and arr[i] == arr[i+1]:
            i += 1
        ans += 1
        i += 1
    return ans


def distinct_count(string):
    arr = list(string)
    arr.sort()
    string = "".join(arr)
    n = len(string)
    i = 0
    ans = ""
    while i < n:
        dis = 1
        while i < n-1 and arr[i] == arr[i+1]:
            dis += 1
            i += 1
        ans += string[i]+str(dis)
        i += 1
    print(ans)


print(distinct([1, 2, 3, 4]))
print(distinct([2, 2, 2, 2, 2]))
distinct_count("aabbc")
distinct_count("sougata")
