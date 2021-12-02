nums: list[int] = []
with open("input.txt") as file:
    prev_bigger_num: int | None = None
    for line in file.readlines():
        nums.append(int(line.strip()))

count = 0
for i in range(3, len(nums)):
    sum1 = nums[i - 3] + nums[i - 2] + nums[i - 1]
    sum2 = nums[i - 2] + nums[i - 1] + nums[i]
    if sum2 > sum1:
        count += 1

print(count)
