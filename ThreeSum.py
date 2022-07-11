def three_sum(lst: list):
    lst.sort()
    print(lst)
    output = set()
    for i in range(len(lst)):
        target = -lst[i]  # first one is the target.
        p_left = i + 1
        p_right = len(lst) - 1
        while p_left < p_right:
            sum_two = lst[p_left] + lst[p_right]  # sum of the two pointer
            if sum_two > target:  # if sum in greater than target , decrease the right pointer.
                p_right -= 1
            elif sum_two < target:  # if sum in smaller than target , increase the left pointer.
                p_left += 1
            else:  # if sum is equal to the target , add the tuple of the target and sum elements in the output set.
                # and decrease the right pointer and increase the left pointer.
                output.add((lst[i], lst[p_left], lst[p_right]))
                p_right -= 1
                p_left += 1
    return list(output)


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    # print(three_sum([0]))
