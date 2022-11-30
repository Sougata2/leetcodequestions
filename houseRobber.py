# Brute force
# check all sub sequences
def house_robber_brute_force(houses, ind=0):
    if ind >= len(houses):
        return 0

    rob_current = houses[ind] + house_robber_brute_force(houses, ind+2)
    rob_next = house_robber_brute_force(houses, ind+1)
    return max(rob_current, rob_next)


# Optimized using memo
# memo keep track of the sub problems.
def house_robber_memoization(houses, ind=0, memo=None):
    if memo == None:
        memo = {}

    if memo.get(ind, None) is not None:
        return memo.get(ind)

    if ind >= len(houses):
        return 0

    rob_current = houses[ind] + house_robber_memoization(houses, ind+2, memo)
    rob_next = house_robber_memoization(houses, ind+1, memo)

    memo[ind] = max(rob_current, rob_next)
    return memo[ind]


print(house_robber_brute_force([2, 7, 9, 3, 1]))
print(house_robber_brute_force([1, 2, 3, 1]))
print()
print(house_robber_memoization([2, 7, 9, 3, 1]))
print(house_robber_memoization([1, 2, 3, 1]))
