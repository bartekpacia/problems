crab_positions: list[int] = []
with open("input.txt") as file:
    crab_positions = list(map(lambda x: int(x), file.readline().split(",")))

min_fuel: int | None = None
for ref_pos in range(len(crab_positions)):
    ref_fuel = 0
    for pos in crab_positions:
        dist = abs(ref_pos - pos)
        fuel = sum(range(dist + 1))
        ref_fuel += fuel

    if min_fuel is None:
        min_fuel = ref_fuel
    elif ref_fuel < min_fuel:
        min_fuel = ref_fuel

print(min_fuel)
