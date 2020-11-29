T = int(input())

results = []
for t in range(1, T + 1):
    N = int(input())
    line2 = input().split()
    chp = [int(x) for x in line2]

    peaks = 0
    for i in range(1, len(chp) - 1):
        prev = chp[i - 1]
        nxt = chp[i + 1]
        if prev < chp[i] and nxt < chp[i]:
            peaks += 1

    results.append("Case #" + str(t) + ": " + str(peaks))

for res in results:
    print(res)
