r0 = 0
r1 = 1

sum = 0
while(r1 < 4_000_001):
    num = r0 + r1
    r0 = r1
    r1 = num

    if num % 2 == 0:
        sum += num

print(sum)
