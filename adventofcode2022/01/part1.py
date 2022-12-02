with open("input.txt") as file:
    max_calories = int(file.readline().strip())
    current_calories = 0
    for l in file:
        line = l.strip()
        if not line:
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
            continue

        calories = int(line)
        current_calories += calories

print(max_calories)
