def combinations(n, k):
    if k > n:
        return []

    ans = []
    temp = []
    traverse(ans, temp, n, k, 0)
    return ans

def traverse(ans, temp, n, k, ind):
    if k == 0:
        ans.append(temp[:])
        return
    
    for i in range(ind, n):
        temp.append(i+1)
        traverse(ans, temp, n, k-1, i+1)
        temp.pop()

print(combinations(4, 2))
    
