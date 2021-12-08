nums: list[int] = []
with open("input.txt") as file:
    nums = [int(line) for line in file.readlines()]

for num1 in nums:
    for num2 in nums:
        if num1 + num2 == 2020:
            print(num1 * num2)
            exit(0)
