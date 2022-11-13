def insert_interval(intervals: list[list[int]], newInterval: list[int]):
    inserted = False
    merged = []
    n = len(intervals)
    for i in range(n):
        if intervals[i][0] > newInterval[0]:
            intervals.insert(i, newInterval)
            inserted = True
            break

    if not inserted:
        intervals.append(newInterval)

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


print(insert_interval([[1, 3], [6, 9]], [2, 5]))
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
