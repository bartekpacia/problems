x = 1

screen: list[list[str]] = [[]]


def on_cycle_end(cycle: int):
    global x

    pos = (cycle - 1) % 40
    if not pos:
        screen.append([])

    i = (cycle - 1) // 40
    sprite_range = range(x - 1, x + 2)
    if pos in sprite_range:
        screen[i].append("#")
    else:
        screen[i].append(".")


cycle = 1
with open("input.txt") as file:
    for l in file:
        line = l.strip()

        instr = line.split()[0]
        if instr == "noop":
            on_cycle_end(cycle)
            cycle += 1
        elif instr == "addx":
            on_cycle_end(cycle)
            cycle += 1
            on_cycle_end(cycle)
            x += int(line.split()[1])
            cycle += 1

for i in range(len(screen)):
    print()
    for j in range(len(screen[i])):
        print(screen[i][j], end="")
