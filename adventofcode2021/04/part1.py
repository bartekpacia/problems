numbers: list[int] = []
boards: list[list[list[int]]] = []

with open("sample.txt") as file:
    numbers = [int(n) for n in file.readline().split(",")]
    file.readline()  # ignore first empty line

    board: list[list[int]] = []
    for line in file:
        line = line.strip()

        if line == "" or line == "\n":
            boards.append(board)
            board = []
            continue

        row = [int(n) for n in line.split()]
        board.append(row)

    boards.append(board)  # append the last row which is not handled above


def is_winning(board: list[list[int]]) -> bool:
    # check rows
    for i in range(len(board)):
        all_correct = True
        for j in range(len(board[i])):
            num = board[i][j]
            if num != -1:
                all_correct = False
                break

        if all_correct:
            return True

    # check columns
    for i in range(len(board)):
        all_correct = True
        for j in range(len(board[i])):
            num = board[j][i]
            if num != -1:
                all_correct = False
                break

        if all_correct:
            return True

    return False

for num in numbers:
    pass

for board in boards:
    for i in range(len(board)):
        for j in range(len(board[i])):
            num = str(board[i][j])
            print(f"{num:<3}", end="")
        print()
    print()
