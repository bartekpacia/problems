with open("input.txt") as f:
    lines = [line.strip() for line in f]

open_matches: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

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


line_scores: list[int] = []
for line in lines:
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

    score = 0
    for char in appended:
        score *= 5
        score += scores[char]

    line_scores.append(score)

line_scores.sort()
print(line_scores[(len(line_scores) - 1) // 2])
