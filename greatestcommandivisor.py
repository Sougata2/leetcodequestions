def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(27, 15))
    print(gcd(24, 60))
