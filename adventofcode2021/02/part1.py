commands: list[tuple[str, int]] = []
with open("input.txt") as file:
    for line in file:
        line = line.strip().split()
        move = line[0]
        value = int(line[1])
        commands.append((move, value))

horizonal_position = 0
depth = 0
for move, value in commands:
    if move == "forward":
        horizonal_position += value
    elif move == "down":
        depth += value
    elif move == "up":
        depth -= value

print(horizonal_position * depth)
