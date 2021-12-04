nums_str: list[str] = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        nums_str.append(line)


def mcb(pos: int) -> int | None:
    zeros = 0
    ones = 0
    for j in range(len(nums_str)):
        num_str = nums_str[j]

        if num_str[pos] == "0":
            zeros += 1
        elif num_str[pos] == "1":
            ones += 1

    if zeros > ones:
        return 0
    elif ones > zeros:
        return 1
    else:
        return None


pos = 2
print(f"mcb for {pos=} is {mcb(pos)}")
