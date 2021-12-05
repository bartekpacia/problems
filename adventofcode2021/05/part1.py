from math import sqrt

# list of vectors
vectors: list[tuple[tuple[int, int], tuple[int, int]]] = []

with open("input.txt") as file:
    for line in file:
        seg = line.strip().split("->")
        x1, y1 = tuple(map(lambda x: int(x), seg[0].strip().split(",")))
        x2, y2 = tuple(map(lambda x: int(x), seg[1].strip().split(",")))

        # for now, only consider horizontal and vertical lines
        if x1 != x2 and y1 != y2:
            continue

        v = ((x1, y1), (x2, y2))
        vectors.append(v)


def dist(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    # sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2
    val = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
    return int(sqrt(val))  # will always be int in part 1


def find_line_points(
    point1: tuple[int, int],
    point2: tuple[int, int],
) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        # vertical line
        if y1 < y2:
            while y1 <= y2:
                points.append((x1, y1))
                y1 += 1
        elif y1 > y2:
            while y2 <= y1:
                points.append((x1, y1))
                y1 -= 1
    elif y1 == y2:
        # horizontal line
        if x1 < x2:
            while x1 <= x2:
                points.append((x1, y1))
                x1 += 1
        elif x1 > x2:
            while x2 <= x1:
                points.append((x1, y1))
                x1 -= 1

    return points


matrix: list[list[int]] = []
for i in range(1000):
    matrix.append([])
    for j in range(1000):
        matrix[i].append(0)


for point1, point2 in vectors:
    d = dist(point1, point2)
    points = find_line_points(point1, point2)

    if points:
        for x, y in points:
            matrix[x][y] += 1

overlap_point_count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[j][i] > 1:
            overlap_point_count += 1

print(overlap_point_count)
