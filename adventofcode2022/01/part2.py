with open("input.txt") as file:
    all_calories: list[int] = []
    current_calories = 0
    for l in file:
        line = l.strip()
        if not line:
            all_calories.append(current_calories)
            current_calories = 0
            continue

        calories = int(line)
        current_calories += calories

    all_calories.append(current_calories)


print(sorted(all_calories))
print(sum(sorted(all_calories)[-3:]))
