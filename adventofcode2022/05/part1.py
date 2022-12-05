stacks: list[list[str]] = []
instructions: list[tuple[int, int, int]] = []

with open("sample.txt") as file:    
    matrix: list[list[str]] = []

    reading_instr = False
    for i, l in enumerate(file):
        line = l
        if not line.strip():
            reading_instr = True
            continue
        
        if reading_instr:
            line = line.strip()
            line = line.replace('move ', '')
            line = line.replace('from ', '')
            line = line.replace(' to', '')
            numbers: list[str] = []
            current_number = ''
            for char in line:
                if char.isnumeric():
                    current_number += char
                else:
                    numbers.append(current_number)
                    current_number = ''
            
            numbers.append(current_number)

            numbers_list = [int(n) for n in numbers]
            instr = (numbers_list[0], numbers_list[1]-1, numbers_list[2]-1)
            instructions.append(instr)
        else:
            matrix.append([])
            for char in line:
                matrix[i].append(char)

    for i, char in enumerate(matrix[-1]):
        if char.isnumeric():
            stacks.append([])
            for j in range(len(matrix)-2, -1, -1):
                if matrix[j][i].isalpha():
                    stacks[-1].append(matrix[j][i])
    

for stack in stacks:
    print(stack)

# rearrange stack using on instructions

def move(src: int, dst: int):
    stacks[dst].append(stacks[src].pop())

for instr in instructions:
    print(f'executing instruction {instr}')
    count = instr[0]
    src = instr[1]
    dst = instr[2]
    for i in range(count):
        print(f'moving from {src} to {dst}')
        move(src, dst)


def rearrange(stacks: list[list[str]], instructions: list[tuple[int, int, int]]):

    for i, stack in enumerate(stacks):
        for j, char in enumerate(stack):
            if char.isnumeric():
                stacks[i][j] = stacks[int(char)][0]
                stacks[int(char)][0] = char
                break

for stack in stacks:
    print(stack)

result=''
for stack in stacks:
    result += stack[-1]
print(result)

# for i, _ in enumerate(matrix):
#     for j, _ in enumerate(matrix[i]):
#         print(matrix[i][j], end='')
#     print('')

#for row in containers_layout:
#    print(row)

# converts [D]
#def read_char()
