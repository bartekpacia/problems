trees: list[list[int]] = []

with open("sample.txt") as f:
    for l in f:
        line = l.strip()
        if line:
            trees.append([int(char) for char in line])


visible_trees: set[tuple[int, int]] = set()

# count trees visible from left and right border
for i in range(len(trees)):
    for j in range(len(trees[i])):
        if j == 0:
            visible_trees.add((i, j))

        if j == len(trees[i]) - 1:
            visible_trees.add((i, j))

# count trees visible from top and bottom border
for i in range(len(trees[0])):
    for j in range(len(trees)):
        if j == 0:
            visible_trees.add((j, i))

        if j == len(trees) - 1:
            visible_trees.add((j, i))

# look from left
for i in range(len(trees)):
    current_tallest_tree = trees[i][0]
    for j in range(1, len(trees[i])):
        print(f'checking tree at ({i}, {j})')

        if trees[i][j] <= current_tallest_tree:
            print(f'tree at ({i}, {j}) with height {trees[i][j]} is not taller that {current_tallest_tree}')

            if trees[i][j] > current_tallest_tree:
                current_tallest_tree = trees[i][j]
            continue

        if (i, j) not in visible_trees:
            print(f'tree at ({i}, {j}) with height {trees[i][j]} is visible from left')

        visible_trees.add((i, j))
        if trees[i][j] > current_tallest_tree:
            current_tallest_tree = trees[i][j]

print(len(visible_trees))
