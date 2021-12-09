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


def explore(
    i: int,
    j: int,
    visited: set[tuple[int, int]],
) -> set[tuple[int, int]]:
    if heightmap[i][j] == 9:
        return set()

    point = (i, j)
    if point not in visited:
        visited.add(point)
    else:
        return set()

    if j - 1 >= 0:
        # left
        visited.update(explore(i, j - 1, visited))
    if i - 1 >= 0:
        # top
        visited.update(explore(i - 1, j, visited))
    if j + 1 < len(heightmap[i]):
        # right
        visited.update(explore(i, j + 1, visited))
    if i + 1 < len(heightmap):
        # bottom
        visited.update(explore(i + 1, j, visited))

    return visited


low_points: list[tuple[int, int]] = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        point = heightmap[i][j]
        if is_low_point(i, j):
            low_points.append((i, j))

basins: list[set[tuple[int, int]]] = []
for i, j in low_points:
    basin = explore(i, j, set())
    basins.append(basin)


max_lens = [len(basin) for basin in basins]
max_lens.sort(reverse=True)
print(max_lens[0] * max_lens[1] * max_lens[2])
