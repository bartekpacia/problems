T = int(input())

for t in range(T):
    line = input().split()
    n = int(line[0])
    k = int(line[1])

    nums = []
    for i in range(1, n * k):
        if i % n != 0:
            nums.append(i)

    print(nums[k - 1])
