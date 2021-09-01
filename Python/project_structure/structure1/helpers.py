# Funktions that are going to help calculate prime numbers

import constants as c


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            # Keep on checking
            if num % n == 0:
                # Until you get one False
                return False
    return True


def calculate_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n) and n not in c.SKIP_RANGE:
            primes.append(n)
    return primes
