head_i = 0
head_j = 0

tail_i = 0
tail_j = 0

with open("input.txt") as file:
    for l in file:
        line = l.strip()
        print(line)

        dir, v = line.split()
        val = int(v)

        if dir == "L":
            head_j -= val
        elif dir == "R":
            head_j += val
        elif dir == "U":
            head_i -= val
        elif dir == "D":
            head_i += val


def follow():
    global head_i, head_j
    global tail_i, tail_j

    if head_i == tail_i:
        pass
    elif head_i > tail_i:
        tail_i += 1


print(f"{head_i=}, {head_j=}")
