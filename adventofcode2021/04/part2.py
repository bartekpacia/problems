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


def find_last_winning_board(
    boards: list[list[list[int]]],
) -> tuple[list[list[int]], int]:
    won_boards: set[int] = set()
    win_order: list[tuple[list[list[int]], int]] = []
    for num in numbers:
        for i in range(len(boards)):
            if i in won_boards:
                continue

            boards[i] = [[n if n != num else -1 for n in row] for row in boards[i]]
            if is_winning(boards[i]):
                won_boards.add(i)
                win_order.append((boards[i], num))

    return win_order.pop()


res = find_last_winning_board(boards)
board, num = res
filtered_board = [[n if n != -1 else 0 for n in row] for row in board]
result = sum(sum(row) for row in filtered_board) * num

print(result)
