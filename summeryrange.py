def summery_range(lst):
    start = 0
    end = 0
    ranges = []
    while end < len(lst):
        if end != len(lst) - 1:
            while lst[end] + 1 == lst[end + 1]:
                end += 1
                if end == len(lst) - 1:
                    break
        else:
            start = end

        if start != end:
            ranges.append(f"{lst[start]}->{lst[end]}")
        else:
            ranges.append(f"{lst[start]}")
        end += 1
        start = end
    return ranges


if __name__ == '__main__':
    print(summery_range([0, 1, 2, 4, 5, 6, 8]))
    print(summery_range([0, 2, 3, 4, 6, 8, 9]))
    print(summery_range([]))
