def is_palindrome(string, left, right):
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return is_palindrome(string, left + 1, right - 1)


if __name__ == '__main__':
    print(is_palindrome('racecar', 0, len('racecar')-1))
    print(is_palindrome('aba', 0, len('aba')-1))
    print(is_palindrome('abba', 0, len('abba')-1))
    print(is_palindrome('sougata', 0, len('sougata')-1))
