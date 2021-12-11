with open("input.txt") as f:
    lines = [line.strip() for line in f]

open_matches: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

scores: dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

illegals = {v: 0 for v in open_matches.values()}


for line in lines:
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
                illegals[char] += 1
                break
score = 0
for char, occurences in illegals.items():
    score += scores[char] * occurences

print(score)
