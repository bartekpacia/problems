def d(n):
    sum = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sum += i

    return sum


total_sum = 0
for i in range(10_000):
    print(i)

    a = d(i)
    if a > i and a < 10_000:
        b = d(a)

        if b == i:
            total_sum += a + b

print(total_sum)
