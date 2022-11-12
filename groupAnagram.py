def group_anagram(strs: list[str]):
    str_dict = {}
    for s in strs:
        ch_sum = 0
        sorted_s = sorted(s)
        for ch in sorted_s:
            ch_sum = ch_sum*31 + ord(ch)
        if str_dict.get(ch_sum) is None:
            str_dict[ch_sum] = [s]
        else:
            str_dict.get(ch_sum).append(s)

    return list(str_dict.values())



print(group_anagram(["eat", "bat"]))
print(group_anagram(["eat","tea","tan","ate","nat","bat"]))

