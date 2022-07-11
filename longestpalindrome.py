def expand_from_middle(string, left, right):
    if string is None or left > right:
        return 0
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return right - left - 1


def main(string):
    if string is None or len(string) < 0:
        return ""
    start = 0
    end = 0
    for i in range(len(string)):
        len1 = expand_from_middle(string, i, i)
        len2 = expand_from_middle(string, i, i + 1)
        max_len = max(len2, len1)
        if max_len > end - start:
            start = i - ((max_len-1) // 2)
            end = i + (max_len // 2)

    return string[start:end+1]


if __name__ == '__main__':
    print(main("racecar"))
    print(main("abba"))
    print(main("sougata"))


