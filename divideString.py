def divide_string(s: str, k: int, fill: str) -> list[str]:
    n = len(s)
    l = r = 0
    seperated_string = []
    while r < n:
        group = ""
        if l + k < n:
            r = l + k
        else:
            r = n

        for i in range(l, r):
            if r == n and i == r-1:
                group += s[i]
                group += fill*(k - len(group))
            else:
                group += s[i]

        l = r

        seperated_string.append(group)
    
    return seperated_string


if __name__ == "__main__":
    print(divide_string("abcdefghi", 3, 'x'))
    print(divide_string("abcdefghij", 3, 'x'))
    print(divide_string("", 3, "*"))
