with open("input.txt") as file:
    badges: list[str] = []

    common_in_group: set[str] = set()
    for i, l in enumerate(file):
        line = l.strip()

        chars: set[str] = set()

        for char in line:
            chars.add(char)

        if not common_in_group:
            common_in_group.update(chars)
        else:
            common_in_group = common_in_group.intersection(chars)

        if (i + 1) % 3 == 0:
            badges.append(common_in_group.pop())
            common_in_group.clear()


def to_priority(char: str) -> int:
    if ord("a") <= ord(char) and ord(char) <= ord("z"):
        # char is lowercase
        prio = ord(char) - ord("a") + 1
        return prio
    else:
        # char is uppercase
        prio = ord(char) - ord("A") + 1
        return prio + 26


print(sum(to_priority(char) for char in badges))
