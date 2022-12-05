with open("sample.txt") as file:    
    matrix: list[list[str]] = []
    for i, l in enumerate(file):
        line = l
        if not line.strip():
            break
        
        matrix.append([])
        for char in line:
            matrix[i].append(char)

    stacks: list[list[str]] = []
    for i, char in enumerate(matrix[-1]):
        if char.isnumeric():
            stacks.append([])
            for j in range(len(matrix)-2, -1, -1):
                if matrix[j][i].isalpha():
                    stacks[-1].append(matrix[j][i])
            
            stacks[-1] = stacks[-1]
    

for stack in stacks:
    print(stack)

# for i, _ in enumerate(matrix):
#     for j, _ in enumerate(matrix[i]):
#         print(matrix[i][j], end='')
#     print('')

#for row in containers_layout:
#    print(row)

# converts [D]
#def read_char()
