with open("input.txt") as file:
    common: list[str] = []

    for l in file:
        line = l.strip()

        first_half: set[str] = set()
        second_half: set[str] = set()

        for i, char in enumerate(line):
            if i < len(line) // 2:
                first_half.add(char)
            else:
                second_half.add(char)

        common.append(first_half.intersection(second_half).pop())


def to_priority(char: str) -> int:
    if ord("a") <= ord(char) and ord(char) <= ord("z"):
        # char is lowercase
        prio = ord(char) - ord("a") + 1
        return prio
    else:
        # char is uppercase
        prio = ord(char) - ord("A") + 1
        return prio + 26


print(sum(to_priority(char) for char in common))
