stacks: list[list[str]] = []
instructions: list[tuple[int, int, int]] = []

with open("input.txt") as file:
    matrix: list[list[str]] = []

    reading_instr = False
    for i, l in enumerate(file):
        line = l
        if not line.strip():
            reading_instr = True
            continue

        if reading_instr:
            line = line.strip()
            line = line.replace("move ", "")
            line = line.replace("from ", "")
            line = line.replace(" to", "")
            numbers: list[str] = []
            current_number = ""
            for char in line:
                if char.isnumeric():
                    current_number += char
                else:
                    numbers.append(current_number)
                    current_number = ""

            numbers.append(current_number)

            numbers_list = [int(n) for n in numbers]
            instr = (numbers_list[0], numbers_list[1] - 1, numbers_list[2] - 1)
            instructions.append(instr)
        else:
            matrix.append([])
            for char in line:
                matrix[i].append(char)

    for i, char in enumerate(matrix[-1]):
        if char.isnumeric():
            stacks.append([])
            for j in range(len(matrix) - 2, -1, -1):
                if matrix[j][i].isalpha():
                    stacks[-1].append(matrix[j][i])


def move(src: int, dst: int):
    stacks[dst].append(stacks[src].pop())


for instr in instructions:
    count = instr[0]
    src = instr[1]
    dst = instr[2]
    for i in range(count):
        move(src, dst)


def rearrange(stacks: list[list[str]], instructions: list[tuple[int, int, int]]):

    for i, stack in enumerate(stacks):
        for j, char in enumerate(stack):
            if char.isnumeric():
                stacks[i][j] = stacks[int(char)][0]
                stacks[int(char)][0] = char
                break

result = ""
for stack in stacks:
    result += stack[-1]
print(result)
