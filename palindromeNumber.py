def palindrome(x):
    # if number is negative, not palindrome
    if x < 0:
        return False

    # size of the number , converting the number to string with str() function
    size = len(str(x))
    # the front part --> second half
    second_half = x
    # the rear part --> first half
    first_half = 0

    # traversing the number upto half of the number's length.
    for i in range(int(size/2)):
        remainder = int(second_half % 10)
        first_half = (first_half*10) + remainder
        second_half = int(second_half/10)
    # if size is odd perform an extra  /10 operation to get the second half correctly.
    if size % 2 != 0:
        second_half = int(second_half/10)

    # if both half are same then true else false.
    if first_half == second_half:
        return True
    return False


print(palindrome(121))
print(palindrome(1221))
print(palindrome(-10))
print(palindrome(12321))
