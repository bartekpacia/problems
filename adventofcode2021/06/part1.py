fish: list[int] = []
with open("input.txt") as file:
    fish = list(map(lambda x: int(x), file.readline().split(",")))

days = 80
for d in range(days):
    for i in range(len(fish)):
        if fish[i] == 0:
            # spawn new fish
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1

print(len(fish))
