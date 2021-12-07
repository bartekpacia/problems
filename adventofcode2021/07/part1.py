crab_positions: list[int] = []
with open("input.txt") as file:
    crab_positions = list(map(lambda x: int(x), file.readline().split(",")))

min_pos: int | None = None
min_fuel: int | None = None
for ref_pos in crab_positions:
    ref_fuel = 0
    for pos in crab_positions:
        fuel = abs(ref_pos - pos)
        if ref_pos == 2:
            print(f"Move from {pos} to {ref_pos}: {fuel} fuel")
        ref_fuel += fuel

    print(f"{ref_fuel=}")
    if min_fuel is None:
        min_pos = ref_pos
        min_fuel = ref_fuel
    elif ref_fuel < min_fuel:
        print("ref_fuel < min_fuel")
        min_pos = ref_pos
        min_fuel = ref_fuel


# mapping of position to crab count in that position
# crabs: dict[int, int] = {}
# for ref_pos in crab_positions:
#     if ref_pos not in crabs:
#         crabs[ref_pos] = 1
#     else:
#         crabs[ref_pos] += 1

print(min_pos, min_fuel)
