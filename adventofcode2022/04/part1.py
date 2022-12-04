def overlaps(a: range, b: range) -> bool:
    starts_earlier = "both"

    if a.start < b.start:
        starts_earlier = "a"
    elif b.start < a.start:
        starts_earlier = "b"

    if a.stop >= b.stop and (starts_earlier == "a" or starts_earlier == "both"):
        # `a` overlaps whole `b`
        return True
    if b.stop >= a.stop and (starts_earlier == "b" or starts_earlier == "both"):
        # `b` overlaps whole `a`
        return True

    return False


overlapping_pairs = 0
with open("input.txt") as file:
    for l in file:
        line = l.strip().split(",")
        start1, end1 = list(map(lambda x: int(x), line[0].split("-")))
        start2, end2 = list(map(lambda x: int(x), line[1].split("-")))

        if overlaps(range(start1, end1 + 1), range(start2, end2 + 1)):
            overlapping_pairs += 1

print(overlapping_pairs)
