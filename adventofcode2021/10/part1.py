with open("sample.txt") as f:
    lines = [line.strip() for line in f]

open_matches: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

close_matches = {v: k for k, v in open_matches.items()}


for line in lines:
    # ignore incomplete lines
    if len(line) % 2 != 0:
        continue

    stack: list[str] = []
    for char in line:
        if char in open_matches.keys():
            # opening brace
            stack.append(char)
        else:
            # closing brace
            if char == open_matches[stack[-1]]:
                print(f"closing brace: {char=}")
                stack.pop()
            else:
                print(f"Expected {open_matches[stack[-1]]}, but found {char} instead")
                break
