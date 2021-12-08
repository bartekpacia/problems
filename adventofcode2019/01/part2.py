with open("input.txt") as file:
    lines = [int(line) for line in file.readlines()]


def calc_fuel_for_module(mass: int) -> int:
    fuel = int(mass / 3) - 2

    if fuel > 0:
        return fuel + calc_fuel_for_module(fuel)
    else:
        return 0


sum = 0
for mass in lines:
    sum += calc_fuel_for_module(mass)

print(sum)
