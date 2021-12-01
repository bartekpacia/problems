nums: list[int] = []
with open("input.txt") as file:
    prev_bigger_num: int | None = None
    for line in file.readlines():
        nums.append(int(line.strip()))

count = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)
