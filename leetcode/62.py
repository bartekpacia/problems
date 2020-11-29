m = 3
n = 2
mx = [[0 for x in range(m)] for y in range(n)]
# fill ones on sides
for i in range(len(mx) - 1):
    mx[i][m - 1] = 1

for i in range(m):
    mx[n - 1][i] = 1

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        mx[i][j] = mx[i + 1][j] + mx[i][j + 1]


print(mx[0][0])
