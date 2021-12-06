# fish age to fish count mapping
fish_ages: dict[int, int] = {}

# fill with 0
for i in range(9):
    fish_ages[i] = 0


def print_ages():
    for i in range(8, -1, -1):
        print(f"{i}: {fish_ages[i]}")


with open("input.txt") as file:
    ages = list(map(lambda x: int(x), file.readline().split(",")))

    for age in ages:
        if age not in fish_ages:
            fish_ages[age] = 1
        else:
            fish_ages[age] += 1

days = 256
fish_with_age_0_from_last_day = 0
for d in range(days):
    print(f"day {d} ---")
    print_ages()

    fish_ages[0] = fish_ages[1]
    fish_ages[1] = fish_ages[2]
    fish_ages[2] = fish_ages[3]
    fish_ages[3] = fish_ages[4]
    fish_ages[4] = fish_ages[5]
    fish_ages[5] = fish_ages[6]
    fish_ages[6] = fish_ages[7]
    fish_ages[7] = fish_ages[8]
    fish_ages[8] = 0

    fish_ages[8] = fish_ages[8] + fish_with_age_0_from_last_day
    fish_ages[6] = fish_ages[6] + fish_with_age_0_from_last_day

    fish_with_age_0_from_last_day = fish_ages[0]

fish_count = 0
for v in fish_ages.values():
    fish_count += v

print(fish_count)
