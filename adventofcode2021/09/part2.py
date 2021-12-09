visited: set[tuple[int, int]] = set()
basin: list[tuple[int, int]] = []

with open("sample.txt") as file:
    heightmap = [[int(num) for num in row.strip()] for row in file.readlines()]


def explore(i: int, j: int):
    print(f"explore {i=} {j=}")
    if heightmap[i][j] == 9:
        return

    point = (i, j)
    if point not in visited:
        visited.add(point)
    else:
        return
    # basin.append(point)

    if j - 1 >= 0:  # left
        explore(i, j - 1)
    if i - 1 >= 0:  # top
        explore(i - 1, j)
    if j + 1 < len(heightmap[i]):  # right
        explore(i, j + 1)
    if i + 1 < len(heightmap):  # bottom
        explore(i + 1, j)


ii = 4
jj = 1
explore(ii, jj)
print(f"EXPLORATION END, start point ({ii}, {jj})")
print(f"explored basin: {basin}")
print(f"visited: {visited}")


# just print
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if (i, j) in visited:
            print(heightmap[i][j], end="")
        else:
            print(" ", end="")
    print("")
