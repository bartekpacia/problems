n = int(input())

answer = 0
for i in range(n):
    line = input().split(" ")
    a, b, c = [int(x) for x in line]

    if a + b + c >= 2:
        answer += 1

print(answer)
