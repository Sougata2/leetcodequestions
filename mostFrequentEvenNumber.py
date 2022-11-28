def most_freuquent_element(nums):
    hash_map = {}
    most_freuquent = -1
    highest_frequency = 0
    for num in nums:
        if num % 2 == 0:
            hash_map[num] = hash_map.get(num, 0) + 1
    
    for key in hash_map:
        if hash_map[key] > highest_frequency:
            most_freuquent = key
            highest_frequency = hash_map[key]
        elif hash_map[key] == highest_frequency:
            most_freuquent = min(most_freuquent, key)
            highest_frequency = hash_map[key]

    return most_freuquent

print(most_freuquent_element([0, 1, 2, 2, 4, 4, 1]))
print(most_freuquent_element([4, 4, 4, 9, 2, 4]))
print(most_freuquent_element([29, 47, 21, 41, 13, 37, 25, 7]))
print(most_freuquent_element([8154, 9139, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))