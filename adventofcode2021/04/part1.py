numbers: list[int] = []
boards: list[list[list[int]]] = []

with open("input.txt") as file:
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


def find_winning_board(
    boards: list[list[list[int]]],
) -> tuple[list[list[int]], int] | None:
    for num in numbers:
        for i in range(len(boards)):
            boards[i] = [[n if n != num else -1 for n in row] for row in boards[i]]
            if is_winning(boards[i]):
                return (boards[i], num)

    return None


res = find_winning_board(boards)
if not res:
    # Just to make Pylance happy. Will never happen.
    exit(1)

winning_board, num = res
filtered_board = [[n if n != -1 else 0 for n in row] for row in winning_board]
result = sum(sum(row) for row in filtered_board) * num

print(result)
