with open("input.txt") as f:
    nums = [int(l) for l in f.readline().split(",")]

i = 0

# to restore "1202 program alarm" state
nums[1] = 12
nums[2] = 2

while True:
    opcode = nums[i]
    if opcode == 1:
        num1 = nums[nums[i + 1]]
        num2 = nums[nums[i + 2]]
        nums[nums[i + 3]] = num1 + num2
    elif opcode == 2:
        num1 = nums[nums[i + 1]]
        num2 = nums[nums[i + 2]]
        nums[nums[i + 3]] = num1 * num2
    else:  # opcode = 99
        break

    i += 4

print(nums[0])
