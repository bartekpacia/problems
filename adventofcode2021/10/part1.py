with open("sample.txt") as f:
    lines = [line.strip() for line in f]

for line in lines:
    # ignore incomplete lines
    if len(line) % 2 != 0:
        continue

    stack_1: list[str] = [] # (
    stack_2: list[str] = [] # [
    stack_3: list[str] = [] # {
    stack_4: list[str] = [] # <
    
    for char in line:
        # (
        if char == "(":
            stack_1.append(char)
        elif char == ")":
            stack_1.pop()

        # [
        if char == "[":
            stack_2.append(char)
        elif char == "]":
            stack_2.pop()

        # {
        if char == "{":
            stack_2.append(char)
        elif char == "}":
            stack_2.pop()
        
        # <
        if char == "<":
            stack_2.append(char)
        elif char == ">":
            stack_2.pop()
