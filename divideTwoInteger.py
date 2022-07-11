def divide_two_integer(dividend, divisor):
    quotient = dividend / divisor
    if quotient > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if quotient < -2 ** 31:
        return -2 ** 31

    return int(quotient)


if __name__ == '__main__':
    print(divide_two_integer(10, 3))
    print(divide_two_integer(7, -3))
