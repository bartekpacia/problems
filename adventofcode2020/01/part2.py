nums: list[int] = []
with open("input.txt") as file:
    nums = [int(line) for line in file.readlines()]

for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
                exit(0)
