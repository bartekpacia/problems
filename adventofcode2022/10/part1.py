signal_strength_sum = 0
x = 1
cycle = 1


def on_cycle_end(cycle: int):
    global x
    global signal_strength_sum
    if (cycle + 20) % 40 == 0:
        signal_strength = x * cycle
        signal_strength_sum += signal_strength


with open("input.txt") as file:
    for l in file:
        line = l.strip()

        instr = line.split()[0]
        if instr == "noop":
            cycle += 1
            on_cycle_end(cycle)
        elif instr == "addx":
            cycle += 1
            on_cycle_end(cycle)
            x += int(line.split()[1])
            cycle += 1
            on_cycle_end(cycle)

print(signal_strength_sum)
