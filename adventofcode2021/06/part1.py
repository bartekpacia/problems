fish: list[int] = []
with open("input.txt") as file:
    fish = list(map(lambda x: int(x), file.readline().split(",")))

days = 80
print(f"Initial state: {fish}")
for d in range(days):
    for i in range(len(fish)):
        if fish[i] == 0:
            # spawn new fish
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1

    print(f"After {d+1:<3} day: {fish}")

print(f"after {days} days, there will be {len(fish)} fish")
