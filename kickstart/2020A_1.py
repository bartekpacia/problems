T = int(input())

results = []
for i in range(T):
    line1 = input().split()
    N, B = [int(x) for x in line1]

    line2 = input().split()
    costs = [int(x) for x in line2]

    costs.sort()

    houses = 0
    for cost in costs:
        if cost <= B:
            B -= cost
            houses += 1

    results.append(houses)

for i, result in enumerate(results):
    print("Case #" + str(i+1) + ": " + str(result))
# 3
# 4 100
# 20 90 40 90
# 4 50
# 30 30 10 10
# 3 300
# 999 999 999
