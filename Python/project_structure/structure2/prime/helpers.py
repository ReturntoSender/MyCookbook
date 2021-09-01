# Funktions that are going to help calculate prime numbers


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            # Keep on checking
            if num % n == 0:
                # Until you get one False
                return False
    return True
