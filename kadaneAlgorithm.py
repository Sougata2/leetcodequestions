def max_sum_sub_array(array):
    # take first element as the current sum and max sum.
    current_sum = array[0]
    max_sum = array[0]
    for i in range(1, len(array)):
        current_val = array[i]  # get the current value

        # check max --> current value is max or
        # current value added to the current sum is max
        current_sum = max(current_val, current_sum + current_val)
        # check max --> current sum is max or the max sum is max.
        max_sum = max(current_sum, max_sum)
    return max_sum


if __name__ == '__main__':
    print(max_sum_sub_array([1, 2, 3, 5, -1]))
    print(max_sum_sub_array([-5, 4, 6, -3, 4, -1]))
    print(max_sum_sub_array([-1, -2, -3, -4, -5]))
