visited: set[tuple[int, int]] = set()
basins: list[set[tuple[int, int]]] = []

with open("sample.txt") as file:
    heightmap = [[int(num) for num in row.strip()] for row in file.readlines()]


def explore(i: int, j: int) -> set[tuple[int, int]]:
    print(f"explore {i=} {j=}")
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


for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if (i, j) not in visited:
            basin = explore(i, j)
            basins.append(basin)
        else:
            continue


top_1 = None
top_2 = None
top_3 = None
for i, basin in enumerate(basins):
    size = len(basin)

    if not top_1:
        top_1 = size
    elif not top_2:
        top_2 = size
    elif not top_3:
        top_3 = size
    elif size > top_1:
        top_1 = size
    elif size > top_2:
        top_2 = size
    elif size > top_3:
        top_3 = size


print(f"ANSWER: {top_1 * top_2 * top_3}")


basin_index = 0
for basin in basins:
    if not basin:
        continue
    print(f"--BASIN {basin_index}--")
    basin_index += 1
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if (i, j) in basin:
                print(heightmap[i][j], end="")
            else:
                print(" ", end="")

        print(" ")
