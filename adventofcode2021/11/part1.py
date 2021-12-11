matrix: list[list[int]] = []
with open("sample.txt") as f:
    for line in f:
        row = [int(char) for char in line.strip()]
        matrix.append(row)


def update_all():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1


def print_matrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")

        print()


def flash():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j - 1 >= 0:
                # left
                matrix[i][j - 1] += 1

            if j - 1 >= 0 and i - 1 >= 0:
                # left-top
                matrix[j - 1][i - 1] += 1

            if i - 1 >= 0:
                # top
                matrix[i - 1][j] += 1

            if j + 1 < len(matrix[i]):
                # right
                matrix[i][j + 1] += 1
            if i - 1 >= 0 and j + 1 < len(matrix[i]):
                # right-top
                matrix[i - 1][j + 1] += 1

            if i + 1 < len(matrix):
                # bottom
                matrix[i + 1][j] += 1


step = 0
