trees: list[list[int]] = []

with open("input.txt") as f:
    for l in f:
        line = l.strip()
        if line:
            trees.append([int(char) for char in line])


largest_scenic_score = 0


def scenic_score(start_i: int, start_j: int) -> int:
    # look left
    left_trees = 0
    j = start_j - 1
    while start_j != 0 and j >= 0:
        # print(f'looking left from {start_i} {start_j} at ({start_i}, {j}) with height {trees[start_i][j]}')
        left_trees += 1
        if trees[start_i][j] < trees[start_i][start_j]:
            j -= 1
        else:
            break

    # look right
    right_trees = 0
    j = start_j + 1
    while start_j != len(trees[0]) - 1 and j <= len(trees[0]) - 1:
        right_trees += 1
        if trees[start_i][j] < trees[start_i][start_j]:
            j += 1
        else:
            break

    # look bottom
    bottom_trees = 0
    i = start_i + 1
    while start_i != len(trees) - 1 and i <= len(trees) - 1:
        bottom_trees += 1
        if trees[i][start_j] < trees[start_i][start_j]:  # tree is shorter
            i += 1
        else:
            break

    # look up
    up_trees = 0
    i = start_i - 1
    while i != 0 and i >= 0:
        up_trees += 1
        if trees[i][start_j] < trees[start_i][start_j]:
            i -= 1
        else:
            break

    return up_trees * left_trees * bottom_trees * right_trees


for i in range(len(trees)):
    for j in range(len(trees[0])):
        score = scenic_score(i, j)
        if score > largest_scenic_score:
            largest_scenic_score = score

print(largest_scenic_score)
