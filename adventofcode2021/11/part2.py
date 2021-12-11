matrix: list[list[int]] = []
with open("input.txt") as f:
    for line in f:
        row = [int(char) for char in line.strip()]
        matrix.append(row)


def do_step():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 9 and (i, j) not in already_flashed:
                flash(i, j)

    for i, j in already_flashed:
        matrix[i][j] = 0


already_flashed: set[tuple[int, int]] = set()


def flash(i: int, j: int):
    """
    Increases the energy of all elements adjacent to [i][j] (there are max 8 of
    them) by 1.
    """
    already_flashed.add((i, j))
    if j - 1 >= 0:
        # left
        matrix[i][j - 1] += 1
        if matrix[i][j - 1] > 9 and (i, j - 1) not in already_flashed:
            flash(i, j - 1)

    if i - 1 >= 0 and j - 1 >= 0:
        # left-top
        matrix[i - 1][j - 1] += 1
        if matrix[i - 1][j - 1] > 9 and (i - 1, j - 1) not in already_flashed:
            flash(i - 1, j - 1)

    if i - 1 >= 0:
        # top
        matrix[i - 1][j] += 1
        if matrix[i - 1][j] > 9 and (i - 1, j) not in already_flashed:
            flash(i - 1, j)

    if i - 1 >= 0 and j + 1 < len(matrix[i]):
        # right-top
        matrix[i - 1][j + 1] += 1
        if matrix[i - 1][j + 1] > 9 and (i - 1, j + 1) not in already_flashed:
            flash(i - 1, j + 1)

    if j + 1 < len(matrix[i]):
        # right
        matrix[i][j + 1] += 1
        if matrix[i][j + 1] > 9 and (i, j + 1) not in already_flashed:
            flash(i, j + 1)

    if i + 1 < len(matrix) and j + 1 < len(matrix[i]):
        # right-bottom
        matrix[i + 1][j + 1] += 1
        if matrix[i + 1][j + 1] > 9 and (i + 1, j + 1) not in already_flashed:
            flash(i + 1, j + 1)

    if i + 1 < len(matrix):
        # bottom
        matrix[i + 1][j] += 1
        if matrix[i + 1][j] > 9 and (i + 1, j) not in already_flashed:
            flash(i + 1, j)

    if i + 1 < len(matrix) and j - 1 >= 0:
        # left-bottom
        matrix[i + 1][j - 1] += 1
        if matrix[i + 1][j - 1] > 9 and (i + 1, j - 1) not in already_flashed:
            flash(i + 1, j - 1)


i = 0
while True:
    if len(already_flashed) == len(matrix) * len(matrix):
        print(i)
        break

    already_flashed.clear()
    do_step()
    i += 1
