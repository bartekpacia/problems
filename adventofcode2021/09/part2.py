visited: set[tuple[int, int]] = set()
basins: list[set[tuple[int, int]]] = []

with open("input.txt") as file:
    heightmap = [[int(num) for num in row.strip()] for row in file.readlines()]


def is_low_point(i: int, j: int) -> bool:
    point = heightmap[i][j]
    adjacent_points: list[int] = []
    if j - 1 >= 0:
        left = heightmap[i][j - 1]
        adjacent_points.append(left)

    if i - 1 >= 0:
        top = heightmap[i - 1][j]
        adjacent_points.append(top)

    if j + 1 < len(heightmap[i]):
        right = heightmap[i][j + 1]
        adjacent_points.append(right)

    if i + 1 < len(heightmap):
        bottom = heightmap[i + 1][j]
        adjacent_points.append(bottom)

    for adj_point in adjacent_points:
        if not point < adj_point:
            return False

    return True


def explore(i: int, j: int) -> set[tuple[int, int]]:
    if heightmap[i][j] == 9:
        return set()

    new_visited: set[tuple[int, int]] = set()

    point = (i, j)
    if point not in visited:
        visited.add(point)
        new_visited.add(point)
    else:
        return set()

    if j - 1 >= 0:  # left
        new_visited.update(explore(i, j - 1))
    if i - 1 >= 0:  # top
        new_visited.update(explore(i - 1, j))
    if j + 1 < len(heightmap[i]):  # right
        new_visited.update(explore(i, j + 1))
    if i + 1 < len(heightmap):  # bottom
        new_visited.update(explore(i + 1, j))

    return new_visited


low_points: list[tuple[int, int]] = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        point = heightmap[i][j]
        if is_low_point(i, j):
            low_points.append((i, j))

for i, j in low_points:
    if (i, j) not in visited:
        basin = explore(i, j)
        basins.append(basin)
    else:
        continue


max_lens = [len(basin) for basin in basins]
max_lens.sort(reverse=True)
print(max_lens[0] * max_lens[1] * max_lens[2])
