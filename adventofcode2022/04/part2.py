def overlaps(a: range, b: range) -> bool:
    a_set = set(a)

    return len(a_set.intersection(b)) != 0


overlapping_pairs = 0
with open("input.txt") as file:
    for l in file:
        line = l.strip().split(",")
        start1, end1 = list(map(lambda x: int(x), line[0].split("-")))
        start2, end2 = list(map(lambda x: int(x), line[1].split("-")))

        if overlaps(range(start1, end1 + 1), range(start2, end2 + 1)):
            overlapping_pairs += 1

print(overlapping_pairs)
