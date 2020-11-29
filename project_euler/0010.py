import math


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, round(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False

    return True


sum = 0
for i in range(2_000_001):
    if is_prime(i):
        print(i)
        sum += i

print(sum)
