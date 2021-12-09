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


risk = 0
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        point = heightmap[i][j]
        if is_low_point(i, j):
            risk += 1 + point

print(risk)
