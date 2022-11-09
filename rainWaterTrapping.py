def trap_rain_water(heights : list[int]):
    # brute force 
    # time - O(n^2), space = O(n)
    # water can only be trapped if the there is a 
    # block bigger than the current one on both the side
    water = 0
    n = len(heights)
    
    for i in range(n):
        left_max = right_max = heights[i]
        # check right
        for r in range(i, n):
            right_max = max(heights[r], right_max)
        
        # check left
        for l in range(i, -1, -1):
            left_max = max(heights[l], left_max)
    
        water += min(left_max, right_max) - heights[i]
    
    return water

def trap_rain_water_fast(heights : list[int]):
    # preprocessing the heights array
    # left array - store the max height that are left to the current index
    # right array - store the max height that are right to the current index
    water = 0
    n = len(heights)
    left_array = []
    left_max = heights[0]
    right_array = []
    right_max = heights[-1]
    for i in range(n):
        left_max = max(left_max, heights[i])
        left_array.append(left_max)
    
    for i in range(n-1, -1, -1):
        right_max = max(right_max, heights[i])
        right_array.insert(0, right_max)

    for h in range(n):
        water += min(left_array[h], right_array[h]) - heights[h]

    return water




print(trap_rain_water([3, 1, 2, 4, 0, 1, 3, 2]))
print(trap_rain_water_fast([3, 1, 2, 4, 0, 1, 3, 2]))
        