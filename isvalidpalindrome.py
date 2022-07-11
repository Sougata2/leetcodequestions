def is_valid_palindrome(txt: str):
    txt = txt.strip()
    left = 0
    right = len(txt) - 1
    while left < right:
        while not txt[left].isalnum():
            if left == len(txt)-1:
                break
            else:
                left += 1
        while not txt[right].isalnum():
            if right == 0:
                break
            else:
                right -= 1
        if left >= right:
            break
        if txt[left].casefold() != txt[right].casefold():
            return False
        right -= 1
        left += 1

    return True


if __name__ == '__main__':
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))
    print(is_valid_palindrome("race a car"))
    print(is_valid_palindrome(".,"))
    print(is_valid_palindrome("0P"))
