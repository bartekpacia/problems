with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

executed: set[int] = set()


def parse(current: int, acc: int) -> int:
    if current in executed:
        return acc

    executed.add(current)

    line = lines[current].split()
    cmd = line[0]
    num = int(line[1])
    if cmd == "nop":
        return parse(current + 1, acc)
    elif cmd == "acc":
        acc += num
        return parse(current + 1, acc)
    else:  # cmd == "jmp"
        return parse(current + num, acc)


print(parse(0, 0))
