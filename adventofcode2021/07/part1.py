crab_positions: list[int] = []
with open("sample.txt") as file:
    crab_positions = list(map(lambda x: int(x), file.readline().split(",")))

# mapping of position to crab count in that position
crabs: dict[int, int] = {}
for pos in crab_positions:
    if pos not in crabs:
        crabs[pos] = 1
    else:
        crabs[pos] += 1

print(crabs)
