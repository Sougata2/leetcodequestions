def longest_increasing_subsequence(array):
    if array is None or len(array) < 1:
        return []

    start = 0
    end = 0
    max_len = end - start + 1
    start_end_guide = []
    for i in range(len(array)):
        if i > 0 and array[i] <= array[i-1]:
            end = i
            if end - start + 1 > max_len:
                start_end_guide.append((start, end))
                max_len = end - start + 1
            start = i
    final_start, final_end = start_end_guide[-1]
    return array[final_start: final_end]


if __name__ == '__main__':
    print(longest_increasing_subsequence([1, 2, 3, 5, 4, 7]))
    print(longest_increasing_subsequence([2, 2, 2, 2, 2, 2]))
