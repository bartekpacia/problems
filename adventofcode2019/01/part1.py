with open("input.txt") as file:
    lines = [int(line) for line in file.readlines()]

sum = 0
for mass in lines:
    fuel = int(mass / 3) - 2
    sum += fuel

print(sum)
