lines: list[str] = []


def parse_instruction(line: str) -> tuple[str, int]:
    line = line.split()
    cmd = line[0]
    num = int(line[1])

    return cmd, num


def parse(acc: int, executed: set[int], prev: int, current: int) -> int | None:
    # if not executed:
    #  print("empty")
    # else:
    #  print(f"size of executed is {len(executed)}")

    if current == len(lines):
        return acc

    if current in executed:
        # print(f"abort")
        return

    executed.add(current)
    cmd, num = parse_instruction(lines[current])

    if cmd == "nop":
        res = parse(acc, executed, current, current + 1)
    elif cmd == "acc":
        res = parse(acc + num, executed, current, current + 1)
    elif cmd == "jmp":
        res = parse(acc, executed, current, current + num)

    return res


def generate_all_possible_sets() -> list[list[str]]:
    test_lists: list[list[str]] = []

    for j in range(len(lines)):
        line = lines[j]
        cmd, num = parse_instruction(line)
        if cmd == "nop":
            new_list: list[str] = lines.copy()
            new_list[j] = f"jmp {num:+}"
            test_lists.append(new_list)
        elif cmd == "jmp":
            new_list: list[str] = lines.copy()
            new_list[j] = f"nop {num:+}"
            test_lists.append(new_list)
        else:
            continue

    return test_lists


def main():
    global lines
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    test_lists = generate_all_possible_sets()
    for l in test_lists:
        # reset global state
        lines = l

        acc = parse(0, set(), 0, 0)
        if acc:
            print(f"{acc=}")


main()
