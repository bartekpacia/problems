with open("sample.txt") as f:
    lines = [line.strip() for line in f]

open_matches: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

close_matches = {v: k for k, v in open_matches.items()}

scores: dict[str, int] = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def is_corrupted_line(line: str) -> bool:
    stack: list[str] = []
    for char in line:
        if char in open_matches.keys():
            # opening brace
            stack.append(char)
        else:
            # closing brace
            if char == open_matches[stack[-1]]:
                stack.pop()
            else:
                return True

    return False


score = 0
corrupted_line_count = 0
for i, line in enumerate(lines):
    if is_corrupted_line(line):
        continue

    stack: list[str] = []
    appended: list[str] = []
    j = 0
    while True:
        if j < len(line):
            char = line[j]
            if char in open_matches.keys():
                # opening brace
                stack.append(char)
            else:
                # closing brace
                if char == open_matches[stack[-1]]:
                    stack.pop()
        else:
            if stack:
                appended.append(open_matches[stack.pop()])
            else:
                break

        j += 1

    fix = "".join(appended)
    print(f"{line} - Complete by adding {fix}")


# print(corrupted_line_count)
