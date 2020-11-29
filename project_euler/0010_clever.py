import math

limit = 2_000_000


def sieve_of_eratosthenes(limit):
    nums = [True] * limit
    nums[0] = False
    nums[1] = False

    for (i, is_prime) in enumerate(nums):
        print(f"i: {i}, is_prime: {is_prime}")
        if is_prime:
            for n in range(i**2, limit, i):
                nums[n] = False

    return nums


nums = sieve_of_eratosthenes(limit)

sum = 0
for i in range(limit):
    if nums[i] is True:
        print(i)
        sum += i

print(sum)
