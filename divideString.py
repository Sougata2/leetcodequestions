def divide_string(s: str, k: int, fill: str) -> list[str]:
    n = len(s)
    l = r = 0
    seperated_string = []
    while r < n:
        # grouping the s by k
        group = ""

        # if the r is greater than equal to n
        # set the r to n
        # if not then r = l + k
        if l + k < n:
            r = l + k
        else:
            r = n

        # adding the char from l to r in the group.
        for i in range(l, r):
            if r == n and i == r-1:
                # if in last group and k char a not present then
                # its replacement will be fill
                # if all are present then fill*(k - len(group)) == 0
                # therefor no change will occurr.
                group += s[i]
                group += fill*(k - len(group))
                break

            group += s[i]

        # shifting the l
        l = r

        # append the group to the main list.
        seperated_string.append(group)

    return seperated_string


if __name__ == "__main__":
    print(divide_string("abcdefghi", 3, 'x'))
    print(divide_string("abcdefghij", 3, 'x'))
    print(divide_string("", 3, "*"))
