with open("input.txt") as file:
    heightmap = [[int(num) for num in row.strip()] for row in file.readlines()]

for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        point = heightmap[i][j]
        print(point, end="")
    print()
