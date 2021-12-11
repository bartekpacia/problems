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

close_matches = {v: k for k, v in open_matches.items()}

illegals = {k: 0 for k, _ in close_matches.items()}


for i, line in enumerate(lines):
    print(f"---------line {i+1}---------")

    stack: list[str] = []
    for char in line:
        if char in open_matches.keys():
            # opening brace
            stack.append(char)
        else:
            # closing brace
            if char == open_matches[stack[-1]]:
                print(f"opened brace {stack[-1]} closed with {char}")
                stack.pop()
            else:
                print(f"Expected {open_matches[stack[-1]]}, but found {char} instead")
                illegals[char] += 1
                break
score = 0
for k, v in illegals.items():
    score += scores[k] * v

print(score)
