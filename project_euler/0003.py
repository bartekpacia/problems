import math

original_num = 600851475143

factors = []
num = original_num


def is_prime(number: int) -> bool:
    if number == 1:
        return False

    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


while(num != 1):
    found = False
    for j in range(2, num + 1):
        if (num % j == 0):
            found = True
            num = int(num / j)
            if is_prime(j):
                factors.append(j)
            break


factors.sort(reverse=True)
print(factors)
