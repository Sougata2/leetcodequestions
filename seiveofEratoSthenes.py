import math


def sieve_of_Eratosthenes(n):
    is_prime = [True for _ in range(n)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        for j in range(2 * i, n, i):
            is_prime[j] = False
    return is_prime


if __name__ == '__main__':
    for x in range(len(sieve_of_Eratosthenes(10))):
        print(f"{x} : {sieve_of_Eratosthenes(10)[x]}")
