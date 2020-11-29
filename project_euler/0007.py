import math


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, round(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False

    return True


found_primes = 0
i = 1
while True:
    if is_prime(i):
        found_primes += 1
        # print(i)

    if found_primes == 10001:
        print(i)
        break

    i += 1
