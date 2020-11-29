line = input().split(" ")
n = int(line[0])
k = int(line[1])

for _ in range(k):
    if n % 10 == 0:
        n /= 10
    else:
        n -= 1

print(int(n))
