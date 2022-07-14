def find_all_permutation(string):
    ans = []
    a = [_ for _ in string]
    r = len(a)
    permute(a, 0, r, ans)
    return ans

def permute(a, l, r, ans):
    if l == r:
        ans.append("".join(a))
    
    for i in range(l, r):
        a[i], a[l] = a[l], a[i]
        permute(a, l+1, r, ans)
        a[i], a[l] = a[l], a[i]


print(find_all_permutation("ABC"))
print(find_all_permutation('123'))
