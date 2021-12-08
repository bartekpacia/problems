with open("input.txt") as f:
    lines = [int(l.strip()) for l in f.readlines()]

lines.sort()


def solve_part_1(lines: list[int]) -> int:
    diffs: dict[int, int] = {}
    for i in range(len(lines)):
        if i == 0:
            prev = 0
        else:
            prev = lines[i - 1]

        current = lines[i]
        diff = current - prev

        if i == len(lines) - 1:
            diffs[3] += 1

        if diff not in diffs:
            diffs[diff] = 1
        else:
            diffs[diff] += 1

    return diffs[1] * diffs[3]


print(solve_part_1(lines))
