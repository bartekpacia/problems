grid_size = int(input("Podaj rozmiar siatki: "))

grid = [[0 for x in range(grid_size + 1)] for x in range(grid_size + 1)]

# fill 2 boundaries with 1s
for i in range(grid_size + 1):
    grid[0][i] = 1
    grid[i][0] = 1

for i in range(1, grid_size + 1):
    for j in range(1, grid_size + 1):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

print(f"Liczba ścieżek: {grid[grid_size][grid_size]}")
