from math import sqrt


def LargestPrime(n):
    if n % 2 == 0:
        n /= 2
        ans = 2
        while n % 2 == 0:
            n /= 2
    else:
        ans = 1
    factor = 3
    maxFactor = sqrt(n)
    while n > 1 and factor <= maxFactor:
        while n % factor == 0:
            n //= factor
            ans = factor
        maxFactor = sqrt(n)
        factor += 2
    if n == 1:
        print(ans)
    else:
        print(n)


LargestPrime(600851475143)
