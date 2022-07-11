def death_circle(n, k):
    if n == 1:
        return 0
    return (death_circle(n - 1, k) + k) % n


if __name__ == '__main__':
    print(death_circle(5, 3))
    print(death_circle(6, 1))
