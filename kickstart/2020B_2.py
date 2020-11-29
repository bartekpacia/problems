T = int(input())

results = []


def biggest_multiple(multiple_of, biggest):
    rest = biggest % multiple_of
    return biggest - rest


for t in range(1, T + 1):
    line1 = input().split()
    line2 = input().split()

    N, D = [int(x) for x in line1]
    buses = [int(x) for x in line2]
    reversed_buses = list(enumerate(buses))

    biggest = float("inf")
    latests = []
    for i, bus in reversed(reversed_buses):
        if len(latests) == 0:
            latest = biggest_multiple(bus, D)
        else:
            latest = biggest_multiple(bus, latests[-1])

        latests.append(latest)

    ans = latests[-1]
    results.append("Case #" + str(t) + ": " + str(ans))

for res in results:
    print(res)
    pass
