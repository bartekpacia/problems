# slow as fuck boi

num = 0
rng = range(2, 21)

while(True):
    required_oks = len(rng)
    oks = 0
    for i in rng:
        if num == 0:
            num += 20
            continue

        print(f"checking {num} % {i}")
        if (num % i) == 0:
            oks += 1
        else:
            num += 20
            break

    if required_oks == oks:
        break


print(num)
